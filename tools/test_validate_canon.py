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
SUPP = RULES.get("supplement_system", {})
IDSYS = RULES["systems"]["id_system"]
SIDFMT = vc.SidFormat(IDSYS["SID_format"])
ECID = [f.upper() for f in IDSYS["ECID_fields"]]
ALIAS = {a.upper(): c.upper()
         for c, al in IDSYS.get("ECID_field_aliases", {}).items() for a in al}


def sid_problems(text):
    out = []
    vc.check_sids("fixture.md", text, SIDFMT, out)
    return out


def csv_problems(content, vt_counter=None):
    out = []
    vt = vt_counter if vt_counter is not None else []
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                     encoding="utf-8", newline="") as fh:
        fh.write(content)
        path = fh.name
    try:
        vc.check_csv(path, SIDFMT, ECID, VOCAB, SUPP, ALIAS, out, vt)
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
    HEADER = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,HEAT,FX,RES,LOAD,BID\n"

    def test_valid_row_passes(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT,H0,FX2,CALM,L0,x\n"
        self.assertEqual(csv_problems(self.HEADER + row), [])

    def test_strain_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT,H0,FX2,STRAIN,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "STRAIN" for p in problems))

    def test_lore_mode_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,LORE,H0,FX2,CALM,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "LORE" for p in problems))

    def test_compound_mode_splits_and_flags_only_the_bad_token(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT / CIV / LORE,H0,FX2,CALM,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        flagged = {p.token for p in problems}
        self.assertIn("LORE", flagged)
        self.assertNotIn("INT", flagged)
        self.assertNotIn("CIV", flagged)

    def test_transition_value_splits_on_arrow(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT,H0,FX2,CALM → STRAIN,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        flagged = {p.token for p in problems}
        self.assertIn("STRAIN", flagged)
        self.assertNotIn("CALM", flagged)

    def test_out_of_range_corridor_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U9,W1,INT,H0,FX2,CALM,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "U9" for p in problems))

    def test_placeholder_row_is_not_flagged_as_vocabulary(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,TODO,TODO,TODO,TODO,TODO,TODO,TODO,x\n"
        problems = [p for p in csv_problems(self.HEADER + row)
                    if p.check == "CHK_VOCAB"]
        self.assertEqual(problems, [])


class TestEcidFields(unittest.TestCase):
    def test_complete_ecid_header_passes(self):
        header = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,HEAT,FX,RES,LOAD,BID\n"
        problems = [p for p in csv_problems(header) if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(problems, [])

    def test_missing_heat_and_fx_are_reported(self):
        # this is the shape of the recovered Book 3 Act III shells
        header = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,RES,LOAD,BID\n"
        problems = [p for p in csv_problems(header) if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(len(problems), 1)
        self.assertIn("HEAT", problems[0].detail)
        self.assertIn("FX", problems[0].detail)

    def test_non_ecid_csv_is_ignored(self):
        header = "breadcrumb_id,type,what_is_hinted,status,notes\n"
        problems = [p for p in csv_problems(header) if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(problems, [])


class TestLoadAxis(unittest.TestCase):
    """The LOAD axis added at decisions 1.4 — where STRAIN's meaning now lives."""

    HEADER = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,HEAT,FX,RES,LOAD,BID\n"

    def test_load_is_in_the_vocabulary(self):
        self.assertEqual(VOCAB["load"], ["L0", "L1", "L2", "L3"])

    def test_valid_load_value_passes(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT,H0,FX2,CALM,L2,x\n"
        self.assertEqual(csv_problems(self.HEADER + row), [])

    def test_out_of_range_load_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT,H0,FX2,CALM,L9,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "L9" for p in problems))

    def test_the_1_5_mapping_migrates_cleanly(self):
        """Every target pair in decisions 1.5 must validate."""
        for res, load in [("CALM", "L2"), ("CALM", "L0"), ("CALM", "L1"),
                          ("SHARD", "L2"), ("SHARD", "L3"),
                          ("RUPTURE", "L3"), ("VT", "L3")]:
            row = (f"S1.T1.B01.A1.E16,Seraphine,Square,U3,W1,INT,H0,FX2,"
                   f"{res},{load},x\n")
            self.assertEqual(csv_problems(self.HEADER + row), [],
                             f"{res}/{load} from decisions 1.5 must validate")


class TestEcidAliases(unittest.TestCase):
    """Decisions 2.4: the schema is canonical, packet labels are input aliases."""

    def test_aliases_are_declared_in_the_rules_file(self):
        self.assertEqual(ALIAS.get("U-LEVEL"), "CORRIDOR")
        self.assertEqual(ALIAS.get("RESONANCE STATE"), "RES")

    def test_packet_labels_satisfy_the_ecid_check(self):
        header = ("SID,POV,ENV,U-Level,WEATHER,MODE,HEAT,FX,"
                  "Resonance State,LOAD,BID\n")
        problems = [p for p in csv_problems(header)
                    if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(problems, [],
                         "U-Level and Resonance State must normalize to "
                         "CORRIDOR and RES")

    def test_values_under_an_alias_are_still_vocabulary_checked(self):
        header = ("SID,POV,ENV,U-Level,WEATHER,MODE,HEAT,FX,"
                  "Resonance State,LOAD,BID\n")
        row = "S1.T1.B01.A1.E16,Seraphine,Square,U9,W1,INT,H0,FX2,STRAIN,L0,x\n"
        flagged = {p.token for p in csv_problems(header + row)}
        self.assertIn("U9", flagged)
        self.assertIn("STRAIN", flagged)


class TestSupplementAxes(unittest.TestCase):
    HEADER = "supplement_id,supplement_type,supplement_function,supplement_vehicle\n"

    def test_ruled_tokens_pass(self):
        self.assertEqual(csv_problems(self.HEADER + "s1,LORE,LINK,CHRON\n"), [])

    def test_provisional_types_are_accepted_not_flagged(self):
        # decisions 7 is applied but unratified; the report names it instead
        self.assertEqual(csv_problems(self.HEADER + "s1,ROM,PING,VEIN\n"), [])

    def test_unknown_type_is_rejected(self):
        problems = csv_problems(self.HEADER + "s1,NONSENSE,LINK,CHRON\n")
        self.assertTrue(any(p.token == "NONSENSE" for p in problems))

    def test_unknown_function_is_rejected(self):
        problems = csv_problems(self.HEADER + "s1,LORE,SHOUT,CHRON\n")
        self.assertTrue(any(p.token == "SHOUT" for p in problems))

    def test_unknown_vehicle_is_rejected(self):
        problems = csv_problems(self.HEADER + "s1,LORE,LINK,TELEGRAM\n")
        self.assertTrue(any(p.token == "TELEGRAM" for p in problems))


class TestVtCap(unittest.TestCase):
    """Decisions 3.4: 10-12 VT Glimpses across all nine books."""

    HEADER = "supplement_id,supplement_type,supplement_function,supplement_vehicle\n"

    def rows(self, n):
        return self.HEADER + "".join(f"s{i},LORE,PING,VT\n" for i in range(n))

    def test_cap_is_read_from_the_rules_file(self):
        self.assertEqual(SUPP["constraints"]["vt_glimpses_max_total"], 12)
        self.assertEqual(SUPP["constraints"]["vt_glimpses_min_total"], 10)

    def test_at_the_cap_is_clean(self):
        vt = []
        csv_problems(self.rows(12), vt)
        out = []
        vc.check_vt_cap(vt, SUPP, out)
        self.assertEqual(out, [])

    def test_over_the_cap_is_reported(self):
        vt = []
        csv_problems(self.rows(14), vt)
        out = []
        vc.check_vt_cap(vt, SUPP, out)
        self.assertEqual(len(out), 2, "one violation per row beyond the cap")
        self.assertEqual(out[0].check, "CHK_VT_CAP")

    def test_under_the_minimum_is_not_a_violation(self):
        # the saga is unwritten; an empty grid is not a defect
        out = []
        vc.check_vt_cap([], SUPP, out)
        self.assertEqual(out, [])

    def test_other_vehicles_do_not_count_toward_the_cap(self):
        vt = []
        csv_problems(self.HEADER + "".join(f"s{i},LORE,PING,CHRON\n"
                                           for i in range(20)), vt)
        self.assertEqual(vt, [])


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

    def test_e00_is_admitted_by_the_current_format(self):
        """Decisions 2.1/2.2: the Prologue is E00."""
        self.assertEqual(sid_problems("S1.T1.B01.A1.E00"), [],
                         "E00 must validate under the widened range")

    def test_e00_would_fail_under_the_old_range(self):
        fmt = vc.SidFormat("S1.T{1-3}.B{01-09}.A{1-3}.E{01-99}")
        out = []
        vc.check_sids("fixture.md", "S1.T1.B01.A1.E00", fmt, out)
        self.assertTrue(out, "the widening is what admits E00, not the matcher")

    def test_book_component_stays_two_digit(self):
        """Ledger 17: B{01-09} applied, B00 flagged rather than adopted."""
        self.assertIn("B{01-09}", IDSYS["SID_format"])
        self.assertTrue(sid_problems("S1.T1.B00.A1.E01"),
                        "B00 is out of range while B{01-09} stands")

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
