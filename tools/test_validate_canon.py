#!/usr/bin/env python3
"""Self-test for tools/validate_canon.py.

The live repository cannot exercise every check — the grids are header-only, so
no CSV row reaches the vocabulary check, and no malformed SID exists in the canon
substrate. Without these fixtures a clean run would be indistinguishable from a
validator that silently does nothing.

Each test feeds a known-bad value and asserts the matching check fires, then feeds
a known-good value and asserts it does not.

    python3 tools/test_validate_canon.py

Standard library only.
"""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_canon as vc  # noqa: E402

RULES = vc.load_rules()
VOCAB = RULES["controlled_vocab"]
IDSYS = RULES["systems"]["id_system"]
SIDFMT = vc.SidFormat(IDSYS["SID_format"])
ECID = [f.upper() for f in IDSYS["ECID_fields"]]


def sid_problems(text):
    out = []
    vc.check_sids("fixture.md", text, SIDFMT, out)
    return out


def csv_problems(content):
    out = []
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                     encoding="utf-8", newline="") as fh:
        fh.write(content)
        path = fh.name
    try:
        vc.check_csv(path, SIDFMT, ECID, VOCAB, out)
    finally:
        os.unlink(path)
    return out


def json_problems(obj):
    out = []
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                     encoding="utf-8") as fh:
        json.dump(obj, fh)
        path = fh.name
    try:
        vc.check_json(path, VOCAB, out)
    finally:
        os.unlink(path)
    return out


class TestSidFormat(unittest.TestCase):
    def test_valid_full_sid_passes(self):
        self.assertEqual(sid_problems("see S1.T1.B01.A1.E16 here"), [])

    def test_valid_act_id_passes(self):
        # act_overlays use the SID prefix ending at the act component
        self.assertEqual(sid_problems("act_id S1.T1.B01.A1 ok"), [])

    def test_one_digit_book_fails(self):
        problems = sid_problems("S1.T1.B1.A1.E16")
        self.assertEqual(len(problems), 1)
        self.assertEqual(problems[0].check, "CHK_SID_FORMAT")
        self.assertIn("1 digit", problems[0].detail)

    def test_one_digit_episode_fails(self):
        problems = sid_problems("S1.T1.B01.A1.E6")
        self.assertTrue(any("digit" in p.detail for p in problems))

    def test_trilogy_out_of_range_fails(self):
        problems = sid_problems("S1.T4.B01.A1.E16")
        self.assertTrue(any("out of range" in p.detail for p in problems))

    def test_book_out_of_range_fails(self):
        problems = sid_problems("S1.T1.B10.A1.E16")
        self.assertTrue(any("out of range" in p.detail for p in problems))

    def test_act_out_of_range_fails(self):
        problems = sid_problems("S1.T1.B01.A4.E16")
        self.assertTrue(any("out of range" in p.detail for p in problems))

    def test_recovered_book3_form_fails(self):
        # the real Book 3 Act III shells, which use the one-digit book form
        problems = sid_problems("EP14 — S1.T1.B3.A3.E14")
        self.assertEqual(len(problems), 1)

    def test_epilogue_act_token_is_not_matched_as_valid(self):
        # S1.T1.B3.EP.E01 has EP where an act must be; it must not pass as a valid SID
        self.assertEqual(sid_problems("S1.T1.B3.EP.E01"), [],
                         "shape does not match the SID finder at all")
        # documented limitation: a non-numeric act token is not SID-shaped, so the
        # format check cannot see it. Ledger section 15 tracks it as a ruling instead.


class TestVocabularyCsv(unittest.TestCase):
    HEADER = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,HEAT,FX,RES,BID\n"

    def test_valid_row_passes(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT,H0,FX2,CALM,x\n"
        self.assertEqual(csv_problems(self.HEADER + row), [])

    def test_strain_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT,H0,FX2,STRAIN,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "STRAIN" for p in problems))

    def test_lore_mode_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,LORE,H0,FX2,CALM,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "LORE" for p in problems))

    def test_compound_mode_splits_and_flags_only_the_bad_token(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT / CIV / LORE,H0,FX2,CALM,x\n"
        problems = csv_problems(self.HEADER + row)
        flagged = {p.token for p in problems}
        self.assertIn("LORE", flagged)
        self.assertNotIn("INT", flagged)
        self.assertNotIn("CIV", flagged)

    def test_transition_value_splits_on_arrow(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT,H0,FX2,CALM → STRAIN,x\n"
        problems = csv_problems(self.HEADER + row)
        flagged = {p.token for p in problems}
        self.assertIn("STRAIN", flagged)
        self.assertNotIn("CALM", flagged)

    def test_out_of_range_corridor_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U9,W1,INT,H0,FX2,CALM,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "U9" for p in problems))

    def test_placeholder_row_is_not_flagged_as_vocabulary(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,TODO,TODO,TODO,TODO,TODO,TODO,x\n"
        problems = [p for p in csv_problems(self.HEADER + row)
                    if p.check == "CHK_VOCAB"]
        self.assertEqual(problems, [])


class TestEcidFields(unittest.TestCase):
    def test_complete_ecid_header_passes(self):
        header = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,HEAT,FX,RES,BID\n"
        problems = [p for p in csv_problems(header) if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(problems, [])

    def test_missing_heat_and_fx_are_reported(self):
        # this is the shape of the recovered Book 3 Act III shells
        header = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,RES,BID\n"
        problems = [p for p in csv_problems(header) if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(len(problems), 1)
        self.assertIn("HEAT", problems[0].detail)
        self.assertIn("FX", problems[0].detail)

    def test_non_ecid_csv_is_ignored(self):
        header = "breadcrumb_id,type,what_is_hinted,status,notes\n"
        problems = [p for p in csv_problems(header) if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(problems, [])


class TestVocabularyJson(unittest.TestCase):
    def test_valid_envelope_passes(self):
        obj = {"environment_envelope": {"weather_max": "W3", "corridor_max": "U5"}}
        self.assertEqual(json_problems(obj), [])

    def test_bad_weather_token_is_rejected(self):
        obj = {"environment_envelope": {"weather_max": "W9"}}
        problems = json_problems(obj)
        self.assertTrue(any(p.token == "W9" for p in problems))

    def test_todo_placeholder_is_reported_as_unpopulated(self):
        obj = {"escalation_permissions": {"max_weather": "TODO"}}
        problems = json_problems(obj)
        self.assertEqual(len(problems), 1)
        self.assertIn("unpopulated placeholder", problems[0].detail)

    def test_heat_range_list_is_checked_elementwise(self):
        obj = {"era_envelope": {"allowed_heat_range": ["H0", "H9"]}}
        problems = json_problems(obj)
        flagged = {p.token for p in problems}
        self.assertIn("H9", flagged)
        self.assertNotIn("H0", flagged)

    def test_malformed_json_is_reported_not_crashed(self):
        out = []
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                         encoding="utf-8") as fh:
            fh.write("{not valid json")
            path = fh.name
        try:
            vc.check_json(path, VOCAB, out)
        finally:
            os.unlink(path)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].check, "CHK_JSON_PARSE")


class TestRulesAreReadNotHardcoded(unittest.TestCase):
    """The checker must follow canon_rules.json, not an internal copy."""

    def test_sid_format_derives_widths_from_the_pattern(self):
        fmt = vc.SidFormat("S1.T{1-3}.B{01-09}.A{1-3}.E{01-99}")
        self.assertEqual([n[0] for n in fmt.numerics], [1, 2, 1, 2])

    def test_changing_the_pattern_changes_the_rule(self):
        # if the author widened books to three digits, B01 would become invalid
        fmt = vc.SidFormat("S1.T{1-3}.B{001-009}.A{1-3}.E{01-99}")
        out = []
        vc.check_sids("fixture.md", "S1.T1.B01.A1.E16", fmt, out)
        self.assertTrue(any("3" in p.detail for p in out))

    def test_vocabularies_come_from_the_rules_file(self):
        for dim in ("corridors", "weather", "res_states", "modes", "heat", "fx"):
            self.assertIn(dim, VOCAB, f"{dim} missing from canon_rules.json")


if __name__ == "__main__":
    unittest.main(verbosity=2)
