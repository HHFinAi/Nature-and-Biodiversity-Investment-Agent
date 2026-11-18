import json
import unittest
from pathlib import Path

class TestWaterDroughtResilience(unittest.TestCase):
    def test_template_has_spatial_rights_and_outcome_gates(self):
        doc=json.loads((Path(__file__).resolve().parents[1]/"examples/water-drought-resilience-template.json").read_text())
        self.assertEqual(doc["status"],"NEEDS_DATA")
        self.assertIsNone(doc["site"]["watershed_identifier"])
        self.assertIsNone(doc["rights"]["groundwater_rights_document_id"])
        self.assertIsNone(doc["hazards"]["local_event_probability"])
        self.assertFalse(doc["outcomes"]["measured_from_baseline"])
        self.assertFalse(doc["outcomes"]["tradable_nature_credit_verified"])

if __name__=="__main__": unittest.main()
