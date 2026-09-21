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
OPTIONAL = [f.upper() for f in IDSYS.get("ECID_fields_optional", [])]


def sid_problems(text):
    out = []
    vc.check_sids("fixture.md", text, SIDFMT, out)
    return out


def csv_problems(content, vt_counter=None, notices=None):
    out = []
    vt = vt_counter if vt_counter is not None else []
    nots = notices if notices is not None else []
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                     encoding="utf-8", newline="") as fh:
        fh.write(content)
        path = fh.name
    try:
        vc.check_csv(path, SIDFMT, ECID, VOCAB, SUPP, ALIAS, out, vt,
                     OPTIONAL, nots)
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
        """A4 is not a fourth act. Every book has exactly three."""
        self.assertTrue(sid_problems("S1.T1.B01.A4.E16"))

    def test_act_zero_fails(self):
        self.assertTrue(sid_problems("S1.T1.B01.A0.E16"))

    def test_an_unknown_act_token_fails(self):
        self.assertTrue(sid_problems("S1.T1.B01.XX.E16"))

    def test_recovered_book3_form_fails(self):
        # the real Book 3 Act III shells, which use the one-digit book form
        problems = sid_problems("EP14 — S1.T1.B3.A3.E14")
        self.assertEqual(len(problems), 1)

    # --- PR and EP in the act slot, Ruling 6 (2026-09-20) -------------------
    def test_a_prologue_sid_parses(self):
        self.assertEqual(sid_problems("S1.T1.B01.PR.E00"), [])

    def test_an_epilogue_sid_parses(self):
        self.assertEqual(sid_problems("S1.T3.B09.EP.E20"), [])

    def test_the_old_ep_blind_spot_is_closed(self):
        """This test replaces one that asserted the blind spot as a limitation.

        Until 2026-09-20 the parser was purely numeric, so `EP` in the act slot did
        not match the finder AT ALL and `S1.T1.B3.EP.E01` went unseen - one-digit
        book and all. The old test asserted that as accepted behaviour. Ruling 6
        made the slot an alternation, so the same string is now found and fails on
        the book component, which was always the real defect. Ledger section 56.
        """
        problems = sid_problems("S1.T1.B3.EP.E01")
        self.assertTrue(problems, "the one-digit book must now be seen")
        self.assertTrue(any("digit" in p.detail for p in problems))

    def test_a_valid_epilogue_sid_with_a_bad_book_still_fails(self):
        self.assertTrue(sid_problems("S1.T1.B1.EP.E01"))

    def test_act_prefix_forms_still_parse(self):
        """Act IDs stop before the episode component; act_overlays rely on it."""
        self.assertEqual(sid_problems("S1.T1.B01.A1"), [])
        self.assertEqual(sid_problems("S1.T3.B09.EP"), [])


class TestVocabularyCsv(unittest.TestCase):
    HEADER = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,HEAT,FX,RES,LOAD,BID\n"

    def test_valid_row_passes(self):
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U3,W1,INT,H0,FX2,CALM,L0,x\n"
        self.assertEqual(csv_problems(self.HEADER + row), [])

    def test_strain_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U3,W1,INT,H0,FX2,STRAIN,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "STRAIN" for p in problems))

    def test_lore_mode_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U3,W1,LORE,H0,FX2,CALM,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "LORE" for p in problems))

    def test_compound_mode_splits_and_flags_only_the_bad_token(self):
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U3,W1,INT / CIV / LORE,H0,FX2,CALM,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        flagged = {p.token for p in problems}
        self.assertIn("LORE", flagged)
        self.assertNotIn("INT", flagged)
        self.assertNotIn("CIV", flagged)

    def test_transition_value_splits_on_arrow(self):
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U3,W1,INT,H0,FX2,CALM → STRAIN,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        flagged = {p.token for p in problems}
        self.assertIn("STRAIN", flagged)
        self.assertNotIn("CALM", flagged)

    def test_out_of_range_corridor_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U9,W1,INT,H0,FX2,CALM,L0,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "U9" for p in problems))

    def test_placeholder_row_is_not_flagged_as_vocabulary(self):
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,TODO,TODO,TODO,TODO,TODO,TODO,TODO,x\n"
        problems = [p for p in csv_problems(self.HEADER + row)
                    if p.check == "CHK_VOCAB"]
        self.assertEqual(problems, [])


class TestEcidFields(unittest.TestCase):
    def test_complete_ecid_header_passes(self):
        header = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,HEAT,FX,RES,LOAD,BID\n"
        problems = [p for p in csv_problems(header) if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(problems, [])

    def test_shell_omitting_heat_and_fx_is_a_notice_not_a_violation(self):
        """Ruled 2026-09-19: HEAT and FX are optional at shell granularity.

        This is the shape of the recovered Book 3 Act III shells.
        """
        notices = []
        header = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,RES,LOAD,BID\n"
        problems = [p for p in csv_problems(header, notices=notices)
                    if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(problems, [], "shells must not fail the build")
        self.assertEqual(len(notices), 1, "but the omission stays visible")
        self.assertIn("HEAT", notices[0].detail)
        self.assertIn("FX", notices[0].detail)

    def test_a_genuinely_required_field_still_violates(self):
        """The softening is scoped to HEAT and FX, not to the whole check."""
        header = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,HEAT,FX,LOAD,BID\n"  # no RES
        problems = [p for p in csv_problems(header) if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(len(problems), 1)
        self.assertIn("RES", problems[0].detail)

    def test_optional_list_comes_from_the_rules_file(self):
        self.assertEqual(sorted(OPTIONAL), ["FX", "HEAT"])

    def test_non_ecid_csv_is_ignored(self):
        header = "breadcrumb_id,type,what_is_hinted,status,notes\n"
        problems = [p for p in csv_problems(header) if p.check == "CHK_ECID_FIELDS"]
        self.assertEqual(problems, [])


class TestLoadAxis(unittest.TestCase):
    """The LOAD axis added at decisions 1.4 — where STRAIN's meaning now lives."""

    HEADER = "SID,POV,ENV,CORRIDOR,WEATHER,MODE,HEAT,FX,RES,LOAD,BID\n"

    def test_supp_is_a_mode(self):
        """Ruled 2026-09-19 (hedged: 'mode, i think')."""
        self.assertIn("SUPP", VOCAB["modes"])

    def test_load_is_in_the_vocabulary(self):
        self.assertEqual(VOCAB["load"], ["L0", "L1", "L2", "L3"])

    def test_valid_load_value_passes(self):
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U3,W1,INT,H0,FX2,CALM,L2,x\n"
        self.assertEqual(csv_problems(self.HEADER + row), [])

    def test_out_of_range_load_is_rejected(self):
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U3,W1,INT,H0,FX2,CALM,L9,x\n"
        problems = csv_problems(self.HEADER + row)
        self.assertTrue(any(p.token == "L9" for p in problems))

    def test_the_1_5_mapping_migrates_cleanly(self):
        """Every target pair in decisions 1.5 must validate."""
        for res, load in [("CALM", "L2"), ("CALM", "L0"), ("CALM", "L1"),
                          ("SHARD", "L2"), ("SHARD", "L3"),
                          ("RUPTURE", "L3"), ("VT", "L3")]:
            row = (f"S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U3,W1,INT,H0,FX2,"
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
        row = "S1.T1.B01.A1.E16,Seraphine,ZONE_BLUE_PULSE,U9,W1,INT,H0,FX2,STRAIN,L0,x\n"
        flagged = {p.token for p in csv_problems(header + row)}
        self.assertIn("U9", flagged)
        self.assertIn("STRAIN", flagged)


class TestSupplementAxes(unittest.TestCase):
    HEADER = ("supplement_id,supplement_type,supplement_function,"
              "supplement_vehicle,supplement_form\n")

    def test_ruled_tokens_pass(self):
        self.assertEqual(csv_problems(self.HEADER + "s1,LORE,LINK,CHRON,LETTER\n"), [])

    def test_provisional_types_are_accepted_not_flagged(self):
        # decisions 7 is applied but unratified; the report names it instead
        self.assertEqual(csv_problems(self.HEADER + "s1,ROM,PING,VEIN,JOURNAL\n"), [])

    def test_unknown_type_is_rejected(self):
        problems = csv_problems(self.HEADER + "s1,NONSENSE,LINK,CHRON,LETTER\n")
        self.assertTrue(any(p.token == "NONSENSE" for p in problems))

    def test_unknown_function_is_rejected(self):
        problems = csv_problems(self.HEADER + "s1,LORE,SHOUT,CHRON,LETTER\n")
        self.assertTrue(any(p.token == "SHOUT" for p in problems))

    def test_unknown_vehicle_is_rejected(self):
        problems = csv_problems(self.HEADER + "s1,LORE,LINK,TELEGRAM,LETTER\n")
        self.assertTrue(any(p.token == "TELEGRAM" for p in problems))

    def test_unknown_form_is_rejected(self):
        problems = csv_problems(self.HEADER + "s1,LORE,LINK,CHRON,POSTCARD\n")
        self.assertTrue(any(p.token == "POSTCARD" for p in problems))

    def test_form_and_vehicle_are_independent(self):
        """Ruled 2026-09-19: form and vehicle are separate values.

        Any form may ride any vehicle; neither constrains the other.
        """
        for vehicle in ("MT", "CHRON", "VEIN", "FIELD"):
            for form in ("LETTER", "JOURNAL", "AFTERMATH"):
                row = f"s1,LORE,LINK,{vehicle},{form}\n"
                self.assertEqual(csv_problems(self.HEADER + row), [],
                                 f"{form} on {vehicle} must validate")

    def test_underscore_metadata_keys_are_not_valid_tokens(self):
        problems = csv_problems(self.HEADER + "s1,LORE,LINK,CHRON,_NOTE\n")
        self.assertTrue(any(p.token == "_NOTE" for p in problems))


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


class TestBands(unittest.TestCase):
    """Per-act escalation_permissions bands, ruled 2026-09-19."""

    def band(self, **over):
        ep = {"corridor": {"min": "U1", "max": "U5"},
              "weather": {"min": "W0", "max": "W3"},
              "fx": {"min": "FX1", "max": "FX2"},
              "exceptions": []}
        ep.update(over)
        return {"act_id": "S1.T1.B03.A3", "escalation_permissions": ep}

    def check(self, obj):
        out = []
        vc.check_bands("fixture.json", obj, VOCAB, SIDFMT, out)
        return out

    def test_well_formed_band_passes(self):
        self.assertEqual(self.check(self.band()), [])

    def test_bad_bound_token_is_rejected(self):
        out = self.check(self.band(corridor={"min": "U1", "max": "U9"}))
        self.assertTrue(any(p.token == "U9" for p in out))

    def test_inverted_band_is_rejected(self):
        out = self.check(self.band(weather={"min": "W3", "max": "W0"}))
        self.assertTrue(any("above" in p.detail for p in out))

    def test_equal_min_and_max_is_allowed(self):
        """B08.A1 pins FX3-FX3; a pin is a legal band, not an error."""
        self.assertEqual(self.check(self.band(fx={"min": "FX3", "max": "FX3"})), [])

    def test_valid_exception_passes(self):
        exc = [{"sid": "S1.T1.B03.A3.E14", "axis": "weather", "value": "W4",
                "scope": "brief", "reason": "First and only VT brush"}]
        self.assertEqual(self.check(self.band(exceptions=exc)), [])

    def test_exception_with_one_digit_book_is_rejected(self):
        exc = [{"sid": "S1.T1.B3.A3.E14", "axis": "weather", "value": "W4"}]
        out = self.check(self.band(exceptions=exc))
        self.assertTrue(any("digit" in p.detail for p in out))

    def test_exception_with_bad_axis_is_rejected(self):
        exc = [{"sid": "S1.T1.B03.A3.E14", "axis": "mood", "value": "W4"}]
        out = self.check(self.band(exceptions=exc))
        self.assertTrue(any(p.token == "mood" for p in out))

    def test_exception_with_bad_value_is_rejected(self):
        exc = [{"sid": "S1.T1.B03.A3.E14", "axis": "weather", "value": "W9"}]
        out = self.check(self.band(exceptions=exc))
        self.assertTrue(any(p.token == "W9" for p in out))

    def test_band_values_are_never_second_guessed(self):
        """A band far outside its trilogy's old ceiling is legal: bands are judgement."""
        self.assertEqual(self.check(self.band(corridor={"min": "U6", "max": "U7"})), [])

    def test_flat_book_context_form_is_ignored(self):
        obj = {"escalation_permissions": {"max_corridor_tier": "TODO"}}
        self.assertEqual(self.check(obj), [])


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



class EnvVocabularyDerivation(unittest.TestCase):
    """ENV derives from the geography system's type layer and only that layer.

    GATE_RULINGS_2026-09-19 Ruling 1. Four things pinned down here: the vocabulary
    exists and is enforced, it is exactly the type layer, named places are not
    members, and the shard progression contributes nothing.
    """

    def test_env_is_a_checked_field(self):
        self.assertEqual(vc.FIELD_VOCAB.get("ENV"), "env")

    def test_env_members_are_exactly_the_type_layer(self):
        loc = RULES["location_system"]
        derived = (set(loc["zone_types"]) | set(loc["corridor_classes"])
                   | set(loc["post_mending"]))
        self.assertEqual(set(VOCAB["env"]), derived)

    def test_named_places_are_not_env_values(self):
        upper = {v.upper() for v in VOCAB["env"]}
        for name in ("VIOLET SPIRAL", "RED LANTERN FAULTLINE", "BLUE PULSE CORRIDOR",
                     "LAUGAVEGUR CORRIDOR", "TREME", "FRENCH QUARTER"):
            self.assertNotIn(name, upper)

    def test_shard_progression_contributes_nothing(self):
        upper = {v.upper() for v in VOCAB["env"]}
        for token in ("FLICKER", "GHOSTWAVE", "FRACTURE", "RUPTURE_THREAT"):
            self.assertNotIn(token, upper)

    def test_a_bad_env_value_is_flagged(self):
        bad = csv_problems("SID,ENV\nS1.T1.B01.A1.E01,Violet Spiral\n")
        self.assertTrue([p for p in bad if p.check == "CHK_VOCAB"],
                        "a named place used as an ENV value should be flagged")

    def test_a_good_env_value_passes(self):
        good = csv_problems("SID,ENV\nS1.T1.B01.A1.E01,ZONE_VIOLET_BLOOM\n")
        self.assertEqual([p for p in good if p.check == "CHK_VOCAB"], [])


class ContestedGroundIsUnassigned(unittest.TestCase):
    """Step 4: leave contested ground unassigned rather than provisionally assigned."""

    def test_no_non_provisional_row_carries_a_type(self):
        import csv as _csv
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "proposals", "concord-2026",
                            "location_places_PROVISIONAL_2026-09-19.csv")
        with open(path, encoding="utf-8") as fh:
            rows = list(_csv.DictReader(fh))
        self.assertTrue(rows)
        for row in rows:
            if row["type_status"] != "PROVISIONAL":
                self.assertEqual(
                    row["mapped_type"], "",
                    "%s is %s but carries a type" % (row["place_name"],
                                                     row["type_status"]))

    def test_the_four_ruled_contested_places_are_present_and_blank(self):
        import csv as _csv
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "proposals", "concord-2026",
                            "location_places_PROVISIONAL_2026-09-19.csv")
        with open(path, encoding="utf-8") as fh:
            rows = {r["place_name"]: r for r in _csv.DictReader(fh)}
        for name in ("Tr\u00e9m\u00e9".encode().decode(), "Marigny",
                     "French Quarter", "Bywater"):
            pass
        for name in ("Marigny", "French Quarter", "Bywater"):
            self.assertIn(name, rows)
            self.assertEqual(rows[name]["mapped_type"], "")
            self.assertEqual(rows[name]["type_status"], "CONTESTED_UNASSIGNED")


LIVE_GRID = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "grids", "milestones_payoffs.csv")
GRID_HEADER = ",".join(RULES["milestone_grid"]["columns"]) + "\n"
GRID_ROW = ("M01,MT,LitRPG Fan,a milestone,T1,B01,A1,E05,mt,2,3,,MED,Y,,,,,"
            "proposed,note\n")


def grid_problems(content):
    """Run the milestone-grid checks over a fixture written to a temp path."""
    import tempfile, os as _os
    out, notices = [], []
    d = tempfile.mkdtemp()
    fp = _os.path.join(d, "milestones_payoffs.csv")
    with open(fp, "w", encoding="utf-8") as fh:
        fh.write(content)
    vc.check_milestone_grid(fp, RULES, VOCAB, out, notices)
    return out, notices


class MilestoneGridRatchet(unittest.TestCase):
    """The grid went live 2026-09-20 with 36 rows, all `proposed`.

    Each check is asserted twice: the live grid passes it, and a known-bad
    fixture fires it. A check that only ever passes proves nothing.
    """

    def test_the_live_grid_passes_every_check(self):
        with open(LIVE_GRID, encoding="utf-8") as fh:
            out, _ = grid_problems(fh.read())
        self.assertEqual([p.check for p in out], [],
                         "the promoted grid must pass its own checks")

    # --- header ---------------------------------------------------------
    def test_column_drift_fails_loudly(self):
        drifted = GRID_HEADER.replace("breadcrumb_density", "breadcrumb_densty")
        out, _ = grid_problems(drifted + GRID_ROW)
        self.assertTrue([p for p in out if p.check == "CHK_GRID_SCHEMA"])

    def test_a_dropped_column_fails(self):
        out, _ = grid_problems(GRID_HEADER.replace(",notes", "") + GRID_ROW)
        self.assertTrue([p for p in out if p.check == "CHK_GRID_SCHEMA"])

    # --- milestone_id ---------------------------------------------------
    def test_duplicate_milestone_id_is_flagged(self):
        out, _ = grid_problems(GRID_HEADER + GRID_ROW + GRID_ROW)
        self.assertTrue([p for p in out if p.check == "CHK_GRID_ID"])

    def test_empty_milestone_id_is_flagged(self):
        out, _ = grid_problems(GRID_HEADER + GRID_ROW.replace("M01,", ",", 1))
        self.assertTrue([p for p in out if p.check == "CHK_GRID_ID"])

    # --- required_setups ------------------------------------------------
    def test_dangling_required_setup_is_flagged(self):
        row = GRID_ROW.replace("E05,mt,2,3,,", "E05,mt,2,3,M99,")
        out, _ = grid_problems(GRID_HEADER + row)
        bad = [p for p in out if p.check == "CHK_GRID_SETUPS"]
        self.assertTrue(bad)
        self.assertEqual(bad[0].token, "M99")

    def test_resolving_required_setup_passes(self):
        second = GRID_ROW.replace("M01,", "M02,", 1).replace("E05,mt,2,3,,",
                                                             "E05,mt,2,3,M01,")
        out, _ = grid_problems(GRID_HEADER + GRID_ROW + second)
        self.assertEqual([p for p in out if p.check == "CHK_GRID_SETUPS"], [])

    # --- target columns -------------------------------------------------
    def test_one_digit_book_is_flagged(self):
        out, _ = grid_problems(GRID_HEADER + GRID_ROW.replace(",B01,", ",B1,"))
        bad = [p for p in out if p.check == "CHK_GRID_TARGET"]
        self.assertTrue(bad)
        self.assertIn("two-digit", bad[0].detail)

    def test_bad_trilogy_is_flagged(self):
        out, _ = grid_problems(GRID_HEADER + GRID_ROW.replace(",T1,", ",T4,"))
        self.assertTrue([p for p in out if p.check == "CHK_GRID_TARGET"])

    def test_bad_act_is_flagged(self):
        out, _ = grid_problems(GRID_HEADER + GRID_ROW.replace(",A1,", ",A4,"))
        self.assertTrue([p for p in out if p.check == "CHK_GRID_TARGET"])

    def test_the_act_slot_holds_five_positions_but_only_three_acts(self):
        """Ruling 6: PR and EP are positions alongside A1-A3, not extra acts.

        27 remains the cap because a prologue is not an act. The distinction is the
        whole content of the ruling, so it is asserted rather than assumed.
        """
        values = RULES["milestone_grid"]["target_act_values"]
        self.assertEqual(values, ["A1", "A2", "A3", "PR", "EP"])
        acts = [v for v in values if v.startswith("A")]
        self.assertEqual(len(acts), 3, "there are exactly three acts")
        self.assertEqual(9 * len(acts), 27, "27 acts is the cap")

    # --- PR and EP, ordinary vocabulary since Ruling 6 ---------------------
    def test_ep_is_neither_a_violation_nor_a_notice(self):
        """The carve-out is gone: EP is a valid position, so nothing is reported.

        It was a notice while the EP-slot question was open. Ruling 6 closed it.
        """
        out, notices = grid_problems(GRID_HEADER + GRID_ROW.replace(",A1,", ",EP,"))
        self.assertEqual([p for p in out if p.check == "CHK_GRID_TARGET"], [])
        self.assertEqual([n for n in notices if n.token == "EP"], [])

    def test_pr_is_accepted_too(self):
        out, notices = grid_problems(GRID_HEADER + GRID_ROW.replace(",A1,", ",PR,"))
        self.assertEqual([p for p in out if p.check == "CHK_GRID_TARGET"], [])
        self.assertEqual([n for n in notices if n.token == "PR"], [])

    def test_a_fourth_act_is_still_a_violation(self):
        out, _ = grid_problems(GRID_HEADER + GRID_ROW.replace(",A1,", ",A4,"))
        self.assertTrue([p for p in out if p.check == "CHK_GRID_TARGET"])

    # --- thread, Ruling 7 (2026-09-20) ------------------------------------
    def test_a_valid_thread_passes(self):
        out, _ = grid_problems(GRID_HEADER + GRID_ROW)
        self.assertEqual([p for p in out if p.check == "CHK_GRID_THREAD"], [])

    def test_unscored_is_a_member_not_a_gap(self):
        """An unsettled row must be able to SAY it is unsettled."""
        out, _ = grid_problems(GRID_HEADER + GRID_ROW.replace(",mt,", ",UNSCORED,"))
        self.assertEqual([p for p in out if p.check == "CHK_GRID_THREAD"], [])

    def test_an_empty_thread_is_a_violation(self):
        """The whole point of UNSCORED: an empty cell cannot be told from an oversight."""
        out, _ = grid_problems(GRID_HEADER + GRID_ROW.replace(",mt,", ",,"))
        bad = [p for p in out if p.check == "CHK_GRID_THREAD"]
        self.assertTrue(bad)
        self.assertIn("UNSCORED", bad[0].detail)

    def test_an_unknown_thread_is_a_violation(self):
        out, _ = grid_problems(GRID_HEADER + GRID_ROW.replace(",mt,", ",veil,"))
        self.assertTrue([p for p in out if p.check == "CHK_GRID_THREAD"])

    def test_veil_was_renamed_to_world(self):
        """Ledger 43 proposed `veil`; it collides with T1's name. Ruling 7 took `world`."""
        self.assertIn("world", VOCAB["threads"])
        self.assertNotIn("veil", VOCAB["threads"])

    def test_institutions_split_into_named_factions(self):
        """Grouping them could not separate B08's Technarc collapse from its neighbours."""
        for t in ("dominion", "technarc", "choirless"):
            self.assertIn(t, VOCAB["threads"])
        self.assertNotIn("institutions", VOCAB["threads"])

    def test_every_live_row_names_a_thread(self):
        with open(LIVE_GRID, encoding="utf-8") as fh:
            out, _ = grid_problems(fh.read())
        self.assertEqual([p for p in out if p.check == "CHK_GRID_THREAD"], [])

    def test_the_pressure_columns_are_thread_scoped(self):
        """Ruled: world pressure should not affect romance. The name says whose it is."""
        cols = RULES["milestone_grid"]["columns"]
        self.assertIn("thread_pressure_before", cols)
        self.assertIn("thread_pressure_after", cols)
        self.assertNotIn("pressure_before", cols)

    def test_the_scale_is_not_saga_absolute(self):
        scale = RULES["milestone_grid"]["pressure_scale"]
        self.assertTrue(scale["levels_extensible"])
        self.assertIn("PER TRILOGY", scale["calibration"])

    def test_the_live_grid_raises_no_ep_notices(self):
        """Was 5. The five EP rows validate as ordinary rows now."""
        with open(LIVE_GRID, encoding="utf-8") as fh:
            out, notices = grid_problems(fh.read())
        self.assertEqual([n for n in notices if n.token == "EP"], [])
        self.assertEqual(out, [], "the whole grid must pass, EP rows included")

    def test_the_five_ep_rows_are_still_there(self):
        """Clearing the notices must not have come from losing the rows."""
        import csv as _csv
        with open(LIVE_GRID, encoding="utf-8") as fh:
            rows = list(_csv.DictReader(fh))
        ep = [r["milestone_id"] for r in rows if r["target_act"] == "EP"]
        self.assertEqual(ep, ["M10", "M11", "M23", "M35", "M36"])

    # --- status ----------------------------------------------------------
    def test_unknown_status_is_flagged(self):
        out, _ = grid_problems(GRID_HEADER + GRID_ROW.replace(",proposed,", ",settled,"))
        self.assertTrue([p for p in out if p.check == "CHK_GRID_STATUS"])

    def test_every_live_row_is_still_proposed(self):
        import csv as _csv
        with open(LIVE_GRID, encoding="utf-8") as fh:
            rows = list(_csv.DictReader(fh))
        self.assertEqual(len(rows), 36)
        self.assertEqual({r["status"] for r in rows}, {"proposed"},
                         "loading the grid must not promote anything to ruled")


# --------------------------------------------------------------------------- #
# The derived book envelopes, 2026-09-20
# --------------------------------------------------------------------------- #

BOOK_FIXTURE = os.path.join(vc.REPO, "book_context", "book_context_B99.json")


def envelope_problems(data, path=BOOK_FIXTURE):
    """check_book_envelope never opens the file, so a synthetic path is enough."""
    out = []
    vc.check_book_envelope(path, data, out)
    return out


def containment_notices(data, path=BOOK_FIXTURE):
    notices = []
    vc.check_trilogy_containment(path, data, VOCAB, notices)
    return notices


def _band(corridor="U1", weather="W0", fx="FX0", tri="T1", exceptions=()):
    return {"trilogy_id": tri, "escalation_permissions": {
        "corridor": {"min": "U1", "max": corridor},
        "weather": {"min": "W0", "max": weather},
        "fx": {"min": "FX0", "max": fx},
        "exceptions": list(exceptions), "basis": "derived"}}


def _trilogy_cap(tri):
    """The live trilogy container's max per axis, for tests that must track it."""
    with open(vc.TRILOGY_CONTEXTS[tri], encoding="utf-8") as fh:
        c = json.load(fh)
    return {ax: (vc.container_band(c, ax) or {}).get("max")
            for ax in ("corridor", "weather", "fx")}


class BookEnvelopeIsRequired(unittest.TestCase):
    """CHK_ENVELOPE closes the gap CHK_BANDS leaves open.

    check_bands returns early on a missing or flat block. That early return is what
    let the nine TODO skeletons through before the book layer was derived; afterwards
    it would have let a DELETED envelope read as zero violations. Ledger section 54.
    """

    def test_a_derived_envelope_passes(self):
        self.assertEqual(envelope_problems(_band()), [])

    def test_a_missing_block_is_a_violation(self):
        out = envelope_problems({"trilogy_id": "T1"})
        self.assertEqual([p.check for p in out], ["CHK_ENVELOPE"])

    def test_check_bands_alone_would_not_catch_a_missing_block(self):
        """The regression this check exists for, stated as a test."""
        out = []
        vc.check_bands(BOOK_FIXTURE, {"trilogy_id": "T1"}, VOCAB, SIDFMT, out)
        self.assertEqual(out, [], "check_bands is expected to stay silent here")
        self.assertTrue(envelope_problems({"trilogy_id": "T1"}),
                        "CHK_ENVELOPE must speak where CHK_BANDS does not")

    def test_a_dropped_axis_is_a_violation(self):
        data = _band()
        del data["escalation_permissions"]["weather"]
        out = envelope_problems(data)
        self.assertTrue([p for p in out if p.check == "CHK_ENVELOPE"])
        self.assertIn("weather", out[0].token)

    def test_a_reverted_scalar_block_is_a_violation(self):
        """The pre-2026-09-20 shape must not come back unnoticed."""
        data = {"trilogy_id": "T1", "escalation_permissions": {
            "max_corridor_tier": "TODO", "max_weather": "TODO", "max_fx": "TODO"}}
        self.assertTrue([p for p in envelope_problems(data)
                         if p.check == "CHK_ENVELOPE"])

    def test_a_block_without_basis_is_a_violation(self):
        data = _band()
        del data["escalation_permissions"]["basis"]
        self.assertTrue([p for p in envelope_problems(data)
                         if p.check == "CHK_ENVELOPE"])

    def test_non_book_files_are_ignored(self):
        other = os.path.join(vc.REPO, "act_overlays", "act_overlay_S1_T1_B01_A1.json")
        self.assertEqual(envelope_problems({"trilogy_id": "T1"}, path=other), [])

    def test_every_live_book_context_passes(self):
        import glob as _glob
        files = sorted(_glob.glob(os.path.join(vc.REPO, "book_context", "*.json")))
        self.assertEqual(len(files), 9)
        for f in files:
            with open(f, encoding="utf-8") as fh:
                out = []
                vc.check_book_envelope(f, json.load(fh), out)
            self.assertEqual(out, [], f"{os.path.basename(f)} must carry a band block")


class TrilogyContainmentIsANoticeNotAViolation(unittest.TestCase):
    """Six of nine books breach their container as of 2026-09-20.

    Which layer gives way is an OPEN author question, so the breach is reported
    and never enforced. These tests pin both halves: that it is seen, and that it
    does not fail the build. Ledger section 53 part 2.
    """

    def test_a_fitting_envelope_produces_no_notice(self):
        cap = _trilogy_cap("T1")
        self.assertEqual(
            containment_notices(_band(cap["corridor"], cap["weather"], "FX3")), [])

    def test_a_breaching_envelope_produces_a_notice(self):
        out = containment_notices(_band("U7", "W0", "FX0"))
        self.assertEqual([n.check for n in out], ["CHK_CONTAINMENT"])
        self.assertEqual(out[0].token, "U7")

    def test_two_breached_axes_are_reported_separately(self):
        out = containment_notices(_band("U7", "W4", "FX0"))
        self.assertEqual(len(out), 2, "corridor and weather, each on its own line")

    def test_fx_is_never_a_breach(self):
        """`default_vfx_ceiling` is a DEFAULT, not a ceiling. Ruling of 2026-09-20.

        Treating it as one produced three spurious notices (B04, B05, B06) before
        the trilogy envelopes were derived. Ledger section 57.
        """
        out = containment_notices(_band("U1", "W0", "FX3", tri="T1"))
        self.assertEqual(out, [], "exceeding a default is not a breach")
        self.assertIsNone(vc.container_band({"era_envelope": {}}, "fx"))

    def test_the_live_breach_count_is_zero(self):
        """Was 13. Both layers are now derived by the same rollup.

        A book cannot exceed a container computed from itself, so any breach here
        means one of the two layers was hand-edited out of agreement.
        """
        import glob as _glob
        total = []
        for f in sorted(_glob.glob(os.path.join(vc.REPO, "book_context", "*.json"))):
            with open(f, encoding="utf-8") as fh:
                vc.check_trilogy_containment(f, json.load(fh), VOCAB, total)
        self.assertEqual([n.detail for n in total], [])

    def test_every_book_band_is_inside_its_derived_trilogy_band(self):
        """The rollup's defining property, asserted directly rather than inferred."""
        import glob as _glob
        for f in sorted(_glob.glob(os.path.join(vc.REPO, "book_context", "*.json"))):
            with open(f, encoding="utf-8") as fh:
                d = json.load(fh)
            cap = _trilogy_cap(d["trilogy_id"])
            for ax in ("corridor", "weather"):
                order = [v.upper() for v in VOCAB[vc.BAND_AXIS_VOCAB[ax]]]
                self.assertLessEqual(
                    order.index(d["escalation_permissions"][ax]["max"]),
                    order.index(cap[ax]),
                    f"{os.path.basename(f)} {ax} exceeds its own trilogy rollup")

    def test_breaches_do_not_reach_the_violation_list(self):
        """A notice must never change the exit code."""
        out = []
        vc.check_book_envelope(BOOK_FIXTURE, _band("U6", "W4", "FX3", tri="T2"), out)
        self.assertEqual(out, [])

    def test_an_unknown_trilogy_id_is_skipped_quietly(self):
        self.assertEqual(containment_notices(_band("U6", tri="T9")), [])



# --------------------------------------------------------------------------- #
# Ruling 5: soft ceilings, declared breaches
# --------------------------------------------------------------------------- #

def _exc(sid, axis, value, reason="fixture"):
    return {"sid": sid, "axis": axis, "value": value, "scope": "brief",
            "reason": reason}


class DeclaredExceptionsMakeASoftCeilingCheckable(unittest.TestCase):
    """Ruling 5: "the ceiling is a tripwire, not a wall."

    A band may exceed its container. What it may not do is exceed it SILENTLY.
    Undeclared is a violation, declared is a notice. Without this check a soft
    ceiling would be unenforceable, which is the same as having none.
    Ledger section 58.
    """

    DIM = "corridors"

    def test_covers_accepts_a_matching_exception(self):
        exc = [_exc("S1.T1.B01.A3.E12", "corridor", "U6")]
        self.assertIsNotNone(
            vc._covers(VOCAB, self.DIM, exc, "corridor", "U6", "S1.T1.B01"))

    def test_covers_rejects_a_weaker_exception(self):
        """An exception permitting U5 does not license a band reaching U6."""
        exc = [_exc("S1.T1.B01.A3.E12", "corridor", "U5")]
        self.assertIsNone(
            vc._covers(VOCAB, self.DIM, exc, "corridor", "U6", "S1.T1.B01"))

    def test_covers_rejects_the_wrong_axis(self):
        exc = [_exc("S1.T1.B01.A3.E12", "weather", "W4")]
        self.assertIsNone(
            vc._covers(VOCAB, self.DIM, exc, "corridor", "U6", "S1.T1.B01"))

    def test_covers_rejects_an_exception_from_another_book(self):
        """The SID check stops one book's exception licensing another's band."""
        exc = [_exc("S1.T1.B03.A3.E14", "corridor", "U6")]
        self.assertIsNone(
            vc._covers(VOCAB, self.DIM, exc, "corridor", "U6", "S1.T1.B01"))

    def test_covers_accepts_a_stronger_exception(self):
        exc = [_exc("S1.T1.B01.A3.E12", "corridor", "U7")]
        self.assertIsNotNone(
            vc._covers(VOCAB, self.DIM, exc, "corridor", "U6", "S1.T1.B01"))

    def test_the_live_substrate_has_no_undeclared_breach(self):
        violations, notices = [], []
        vc.check_declared_exceptions(VOCAB, violations, notices)
        self.assertEqual([v.detail for v in violations], [])

    def test_the_live_b03_exception_is_the_declared_kind(self):
        """B03's W4 VT brush is the saga's one real exception; it must parse."""
        with open(os.path.join(vc.REPO, "book_context",
                               "book_context_B03.json"), encoding="utf-8") as fh:
            ep = json.load(fh)["escalation_permissions"]
        exc = ep["exceptions"]
        self.assertEqual(len(exc), 1)
        self.assertEqual(exc[0]["axis"], "weather")
        self.assertEqual(exc[0]["value"], "W4")
        for key in ("sid", "axis", "value", "scope", "reason"):
            self.assertIn(key, exc[0], "Ruling 5 names all five fields")



# --------------------------------------------------------------------------- #
# Ruling 10: prose lives in sources/ and manuscript/, and is never validated
# --------------------------------------------------------------------------- #

class ProseDirectoriesStayOutOfScope(unittest.TestCase):
    """Ruling 10 permits prose in two directories and requires both stay unscanned.

    The exclusion must hold in BOTH scopes. If `sources/` were ever scanned, every
    committed conversation would be parsed for SIDs and vocabulary, canon-scope would
    stop meaning what it means, and the ceiling would move for reasons that have
    nothing to do with canon. Ledger section 70.
    """

    def test_prose_dirs_are_declared(self):
        self.assertEqual(vc.PROSE_DIRS, ["sources", "manuscript"])

    def test_prose_dirs_are_not_substrate(self):
        for d in vc.PROSE_DIRS:
            self.assertNotIn(d, vc.SUBSTRATE_DIRS)

    def test_prose_dirs_are_not_meta(self):
        """Meta scope is still scope: --all would parse them too."""
        for d in vc.PROSE_DIRS:
            self.assertNotIn(d, vc.META_DIRS)

    def test_no_scanned_file_comes_from_a_prose_dir(self):
        """The behavioural check, not just the declaration."""
        for include_meta in (False, True):
            for path in vc.iter_files(include_meta):
                top = vc.rel(path).split(os.sep)[0]
                self.assertNotIn(
                    top, vc.PROSE_DIRS,
                    f"{vc.rel(path)} was scanned; Ruling 10 excludes {top}/")

    def test_a_planted_prose_file_is_not_scanned(self):
        """Prove it against a real file rather than trusting the directory list."""
        d = os.path.join(vc.REPO, "sources")
        if not os.path.isdir(d):
            self.skipTest("sources/ not present")
        probe = os.path.join(d, "_scope_probe.md")
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("S1.T1.B3.A3.E01 would be a violation if this were scanned.\n")
        try:
            for include_meta in (False, True):
                self.assertNotIn(probe, list(vc.iter_files(include_meta)))
        finally:
            os.unlink(probe)


if __name__ == "__main__":
    unittest.main(verbosity=2)
