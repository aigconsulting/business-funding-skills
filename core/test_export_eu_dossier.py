#!/usr/bin/env python3
"""Regressioni deterministiche del bridge; nessuna rete."""
import unittest
from export_eu_dossier import convert

def fixture():
    return {
        "schema":"business-funding-skills/dossier@v1","dossier_id":"synthetic-1",
        "created":"2026-11-10","updated":"2026-11-10","instrument_types":["GRANT"],
        "opportunity":{"id":"DEMO-AVVISO-1","title":"Demo sintetica","last_checked":"2026-11-10",
          "eu_programme":"PROGRAMMA-DEMO","eu_management_mode":"concorrente","qfp_cycle":"2021-2027"},
        "sources":[{"id":"SRC-1","title":"Documento demo","url":"https://example.org/demo","checked_at":"2026-11-10","state":"DA_CONFERMARE"}],
        "requirements":[{"id":"REQ-1","text":"Condizione demo","source_id":"SRC-1","state":"DA_CONFERMARE"}]
    }

class BridgeTest(unittest.TestCase):
    def test_valid_export_preserves_state(self):
        out=convert(fixture())
        self.assertEqual(out["schema"],"eu-funding-skills/dossier@v1")
        self.assertEqual(out["requisiti"][0]["stato"],"DA_CONFERMARE")
        self.assertEqual(out["opportunita"]["avviso_id"],"DEMO-AVVISO-1")
    def test_equity_refused(self):
        d=fixture();d["instrument_types"]=["EQUITY"]
        with self.assertRaises(ValueError): convert(d)
    def test_hybrid_refused(self):
        d=fixture();d["instrument_types"]=["GRANT","LOAN"]
        with self.assertRaises(ValueError): convert(d)
    def test_source_dangling_refused(self):
        d=fixture();d["requirements"][0]["source_id"]="SRC-NOT-THERE"
        with self.assertRaises(ValueError): convert(d)
    def test_no_silent_project_drop(self):
        d=fixture();d["project"]={"goals":["x"]}
        with self.assertRaises(ValueError): convert(d)
    def test_unverified_programme_refused(self):
        d=fixture();del d["opportunity"]["eu_programme"]
        with self.assertRaises(ValueError): convert(d)
    def test_unverified_requirement_never_upgraded(self):
        d=fixture();d["requirements"][0]["state"]="VERIFICATO"
        with self.assertRaises(ValueError): convert(d)

if __name__=="__main__": unittest.main()
