#Requires -Version 5.1
<#
.SYNOPSIS
  Commit the 2026-09-15 ChatGPT account export into sources/ per Ruling 10.

.DESCRIPTION
  Runs the whole ingest on your PC in one pass, in the order the ruling requires:

    1. verify the repository is clean and up to date
    2. copy MANIFEST.csv and the top-level *.md / *.json into
       sources/chatgpt_export_2026-09/   (the music\ subfolder and the .tar are
       deliberately not copied -- they are supplied separately)
    3. delete the six excluded files BEFORE anything is staged
    4. scan for workspace_account_id BEFORE anything is staged
    5. run tools/verify_sources.py and require exit 0
    6. only then: git add / commit / push

  Any failed check aborts before the first git add. Nothing reaches history
  unless every check passed -- a value committed raw stays in git history
  permanently, so the abort is the safe side of every uncertainty.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File tools\ingest_export.ps1 -DryRun
  powershell -ExecutionPolicy Bypass -File tools\ingest_export.ps1
#>
[CmdletBinding()]
param(
  # Folder holding the loose export files (NOT the .tar -- the files are already
  # extracted beside it, and the .tar is misnamed after one focused conversation).
  [string] $Src = "C:\Users\jamey\OneDrive\Desktop\ChatGPT Backup 26-0915\concord_saga",

  # MANIFEST.csv as supplied.
  [string] $Manifest = "$env:USERPROFILE\Downloads\MANIFEST.csv",

  # Local clone of concord-saga-canon. Defaults to this script's own repository.
  [string] $Repo,

  # Stop after verification; stage, commit and push nothing.
  [switch] $DryRun,

  # Commit but do not push.
  [switch] $NoPush
)

$ErrorActionPreference = 'Stop'

function Say  ($m) { Write-Host $m }
function Ok   ($m) { Write-Host "  OK    $m" -ForegroundColor Green }
function Fail ($m) {
  Write-Host ""
  Write-Host "ABORT  $m" -ForegroundColor Red
  Write-Host "Nothing was staged, committed or pushed." -ForegroundColor Red
  exit 1
}

# ---------------------------------------------------------------- constants --
# The six excluded files. Reasons are in sources/README.md and MANIFEST.csv.
$Excluded = @(
  '2025-11-17__Chat_export_options__691a9879.json'
  '2025-12-31__Archetype_Test_Insightful_or_BS__69559fa4.md'
  '2025-12-31__Archetype_Test_Insightful_or_BS__69559fa4.json'
  '2026-09-14__Review_Project_Status__6aa7fe7e.json'
  '2026-09-14__Story_Summary_Writing__6aa7578e.md'
  '2026-09-14__Story_Summary_Writing__6aa7578e.json'
)
$ExpectCopied   = 144   # 72 conversations x 2
$ExpectCommitted = 138  # after the six exclusions
$CommitMsg = @'
Commit the 2026-09-15 account export: 70 conversations, 138 files, per Ruling 10

Ruling 10 scoped the no-prose rule to the substrate and opened sources/ for
supplied material, verbatim and append-only. This is the account export that
rule was written for.

72 conversations exported; 70 committed as 138 files. Six files are excluded for
session tokens, signed URLs, third-party work contact details, or being another
project -- each keeps its MANIFEST.csv row with hash and reason, so the gap is
visible and auditable against the original TAR. Exclusion, never redaction: a
redacted file would silently break the manifest's promise that every committed
file matches its hash exactly.

Verified with tools/verify_sources.py before this commit: every committed file
present and hash-matched, no excluded, unlisted or forbidden content.
'@

# ------------------------------------------------------------------ locate ---
if (-not $Repo) {
  $Repo = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
}
$Repo = (Resolve-Path -LiteralPath $Repo -ErrorAction SilentlyContinue).Path
if (-not $Repo) { Fail "repository not found. Pass -Repo <path to your clone>." }

$Dest = Join-Path $Repo 'sources\chatgpt_export_2026-09'

Say ""
Say "Repo      $Repo"
Say "Source    $Src"
Say "Manifest  $Manifest"
Say "Dest      $Dest"
Say ""

# --------------------------------------------------------- 1. preflight -----
Say "1. Preflight"

if (-not (Get-Command git    -ErrorAction SilentlyContinue)) { Fail "git is not on PATH." }
$Py = $null
foreach ($c in 'python','py','python3') {
  if (Get-Command $c -ErrorAction SilentlyContinue) { $Py = $c; break }
}
if (-not $Py) { Fail "no python on PATH (tried python, py, python3)." }
Ok "git and $Py found"

if (-not (Test-Path -LiteralPath $Src))      { Fail "source folder not found: $Src" }
if (-not (Test-Path -LiteralPath $Manifest)) { Fail "MANIFEST.csv not found: $Manifest" }
if (-not (Test-Path -LiteralPath (Join-Path $Repo 'tools\verify_sources.py'))) {
  Fail "tools\verify_sources.py not found under $Repo -- is this the right clone?"
}
Ok "source, manifest and verifier all present"

Push-Location $Repo
try {
  $dirty = git status --porcelain
  if ($dirty) {
    Say ""
    $dirty | ForEach-Object { Say "    $_" }
    Fail "working tree is not clean. Commit or stash the above first."
  }
  Ok "working tree clean"

  $branch = (git rev-parse --abbrev-ref HEAD).Trim()
  Say "        on branch $branch -- pulling"
  git pull --ff-only 2>&1 | ForEach-Object { Say "        $_" }
  if ($LASTEXITCODE -ne 0) { Fail "git pull failed. Resolve, then re-run." }
  Ok "up to date with origin/$branch"
} finally { Pop-Location }

# ------------------------------------------------------------- 2. copy ------
Say ""
Say "2. Copy"

if (-not (Test-Path -LiteralPath $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }

$stale = @(Get-ChildItem -LiteralPath $Dest -File | Where-Object { $_.Name -ne 'README.md' })
if ($stale.Count) {
  Say "        clearing $($stale.Count) file(s) already in the destination"
  $stale | Remove-Item -Force
}

Copy-Item -LiteralPath $Manifest -Destination (Join-Path $Dest 'MANIFEST.csv') -Force
Ok "MANIFEST.csv"

# Top level only -- no -Recurse, so music\ is excluded by construction. The .tar
# is not matched by either pattern.
Copy-Item -Path (Join-Path $Src '*.md')   -Destination $Dest -Force -ErrorAction SilentlyContinue
Copy-Item -Path (Join-Path $Src '*.json') -Destination $Dest -Force -ErrorAction SilentlyContinue

$copied = @(Get-ChildItem -LiteralPath $Dest -File |
            Where-Object { $_.Extension -in '.md','.json' -and $_.Name -ne 'README.md' })
Say "        copied $($copied.Count) file(s); expected $ExpectCopied"
if ($copied.Count -ne $ExpectCopied) {
  Say "        (not fatal here -- verify_sources.py names exactly what is wrong)" 
} else { Ok "count matches" }

# ------------------------------------------------- 3. delete the excluded ---
Say ""
Say "3. Delete the six excluded files (before anything is staged)"

$removed = 0
foreach ($n in $Excluded) {
  $p = Join-Path $Dest $n
  if (Test-Path -LiteralPath $p) { Remove-Item -LiteralPath $p -Force; $removed++ }
}
$after = @(Get-ChildItem -LiteralPath $Dest -File |
           Where-Object { $_.Extension -in '.md','.json' -and $_.Name -ne 'README.md' })
Say "        removed $removed of 6; $($after.Count) file(s) remain; expected $ExpectCommitted"
if ($removed -ne 6) { Fail "expected to remove 6 excluded files, removed $removed." }
Ok "exclusions applied"

# -------------------------------------------- 4. workspace_account_id scan --
Say ""
Say "4. Scan for workspace_account_id (before anything is staged)"

$hits = @(Select-String -Path (Join-Path $Dest '*.json') -Pattern 'workspace_account_id' `
            -SimpleMatch -List -ErrorAction SilentlyContinue)
if ($hits.Count) {
  Say ""
  $hits | ForEach-Object { Say "        $($_.Filename)" }
  Say ""
  Say "  Amendment 1 says this key is stripped before the FIRST commit, never"
  Say "  after -- a value committed raw stays in git history permanently."
  Say "  But the manifest hashes cover the files as exported, so redacting them"
  Say "  here would make every one of those rows fail verification."
  Fail "$($hits.Count) file(s) carry workspace_account_id. That collision is a ruling, not a script decision -- send me this list."
}
Ok "0 occurrences"

# ---------------------------------------------------------- 5. verify -------
Say ""
Say "5. Verify against the manifest"

Push-Location $Repo
try {
  & $Py 'tools\verify_sources.py' 2>&1 | ForEach-Object { Say "        $_" }
  $rc = $LASTEXITCODE
} finally { Pop-Location }
if ($rc -ne 0) { Fail "verify_sources.py exited $rc." }
Ok "verifier passed"

if ($DryRun) {
  Say ""
  Write-Host "DRY RUN -- every check passed. Nothing staged. Re-run without -DryRun to commit." -ForegroundColor Cyan
  exit 0
}

# ------------------------------------------------------ 6. commit and push --
Say ""
Say "6. Commit and push"

Push-Location $Repo
try {
  git add sources/
  if ($LASTEXITCODE -ne 0) { Fail "git add failed." }

  $staged = @(git diff --cached --name-only)
  $bad = @($staged | Where-Object { $_ -notlike 'sources/*' })
  if ($bad.Count) {
    git reset | Out-Null
    $bad | ForEach-Object { Say "        $_" }
    Fail "something outside sources/ was staged. Unstaged; nothing committed."
  }
  Say "        staging $($staged.Count) path(s), all under sources/"

  $ignored = @($staged | Where-Object { $Excluded -contains (Split-Path $_ -Leaf) })
  if ($ignored.Count) {
    git reset | Out-Null
    Fail "an excluded file reached the index. Unstaged; nothing committed."
  }
  Ok "no excluded file staged"

  $msgFile = Join-Path $env:TEMP "concord_commit_msg.txt"
  Set-Content -LiteralPath $msgFile -Value $CommitMsg -Encoding UTF8
  git commit -F $msgFile
  $rcCommit = $LASTEXITCODE
  Remove-Item -LiteralPath $msgFile -Force -ErrorAction SilentlyContinue
  if ($rcCommit -ne 0) { Fail "git commit failed." }
  Ok "committed"

  if ($NoPush) {
    Say ""
    Write-Host "Committed, not pushed (-NoPush). Push with:  git push -u origin $branch" -ForegroundColor Cyan
    exit 0
  }

  $pushed = $false
  foreach ($wait in 0,2,4,8,16) {
    if ($wait) { Say "        retrying in ${wait}s"; Start-Sleep -Seconds $wait }
    git push -u origin $branch 2>&1 | ForEach-Object { Say "        $_" }
    if ($LASTEXITCODE -eq 0) { $pushed = $true; break }
  }
  if (-not $pushed) { Fail "push failed after 5 attempts. The commit is safe locally -- retry with: git push -u origin $branch" }
  Ok "pushed to origin/$branch"
} finally { Pop-Location }

Say ""
Write-Host "Done. $ExpectCommitted files committed under sources/chatgpt_export_2026-09/." -ForegroundColor Green
