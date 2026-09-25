import unittest
from sf_agent.analytics import exposure_coverage,additional_outcome,nature_cashflow_stress,cost_per_outcome,conditional_project_revenue
from sf_agent.validation import DataError

class NatureArithmetic(unittest.TestCase):
    def test_unknown_coverage_preserved(self):
        r=exposure_coverage(1,.8,.5,.2);self.assertEqual(r['unassessed_share'],.5);self.assertEqual(r['high_dependency_share_of_total'],.2);self.assertEqual(r['high_dependency_share_of_screened'],.4)
    def test_no_screening_not_zero_dependency(self): self.assertIsNone(exposure_coverage(1,.5,0,0)['high_dependency_share_of_screened'])
    def test_invalid_coverage_nesting(self):
        with self.assertRaises(DataError): exposure_coverage(1,.5,.7,.1)
    def test_zero_denominator(self):
        with self.assertRaises(DataError): exposure_coverage(0,0,0,0)
    def test_additional_outcome(self): self.assertEqual(additional_outcome(120,100,.5),10)
    def test_negative_additional_outcome_preserved(self): self.assertEqual(additional_outcome(80,100,.5),-10)
    def test_invalid_attribution(self):
        with self.assertRaises(DataError): additional_outcome(120,100,1.1)
    def test_financial_transmission(self):
        r=nature_cashflow_stress(100000000,.3,.2,.4,.25,500000,2000000)
        self.assertEqual(r['lost_revenue'],4500000);self.assertEqual(r['free_cashflow_change'],-4300000)
    def test_mitigation_costs_not_ignored(self):
        r=nature_cashflow_stress(100,.3,.2,.4,1,2,3);self.assertEqual(r['lost_revenue'],0);self.assertEqual(r['free_cashflow_change'],-5)
    def test_outcome_cost(self): self.assertEqual(cost_per_outcome(100,50000),500)
    def test_no_outcomes_no_cost_ratio(self):
        with self.assertRaises(DataError): cost_per_outcome(0,50000)
    def test_conditional_revenue(self): self.assertEqual(conditional_project_revenue(1000,.8,10,100,500),7400)
    def test_unprofitable_project_remains_negative(self): self.assertEqual(conditional_project_revenue(10,0,10,100,500),-600)
    def test_invalid_delivery(self):
        with self.assertRaises(DataError): conditional_project_revenue(100,1.2,10,0,0)
if __name__=='__main__': unittest.main()
