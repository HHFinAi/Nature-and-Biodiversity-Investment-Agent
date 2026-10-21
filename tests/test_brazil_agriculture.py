"""Test accounting identities and the farm break-even, not nature causality."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('brazil_case', ROOT / 'examples/brazil-agriculture/model.py')
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
from public_case_support import load


class BrazilCase(unittest.TestCase):
    def test_growth_decomposition_reconciles(self):
        for production, area in [(1.4, 2.3), (10, 0), (-5, 2), (0, 0)]:
            d = model.decompose(production, area)
            self.assertAlmostEqual(d['area_contribution_pp'] + d['yield_contribution_pp'], production)
            self.assertAlmostEqual((1 + area / 100) * (1 + d['yield_growth_percent'] / 100), 1 + production / 100)

    def test_farm_break_even(self):
        i, s = load(ROOT / 'examples/brazil-agriculture')
        d = model.calculate(i, s)
        break_even = d['price_change_at_unchanged_profit_percent'] / 100
        self.assertAlmostEqual(model.farm_stress(i['assumptions'], break_even)['profit_change_percent'], 0, places=5)
        self.assertLess(model.farm_stress(i['assumptions'], -.1)['profit_change_percent'], 0)

    def test_land_arithmetic_preserves_fixed_output(self):
        i, s = load(ROOT / 'examples/brazil-agriculture')
        reduction = model.calculate(i, s)['fixed_output_crop_area_reduction_percent'] / 100
        self.assertAlmostEqual((1 - reduction) * 1.1, 1, places=7)

    def test_invalid_growth_rejected(self):
        with self.assertRaises(ValueError): model.decompose(1, -100)

    def test_archived_results_reproduce(self):
        p = subprocess.run([sys.executable, 'examples/brazil-agriculture/model.py', '--check'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)


if __name__ == '__main__': unittest.main()
