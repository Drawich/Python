import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import unittest
from bill_splitter import BillValidator, BillSplitterService


class TestBillValidator(unittest.TestCase):

    def test_clean_float_with_comma(self):
        """Verify comma vs. dot usage works."""
        self.assertEqual(BillValidator.clean_and_validate_float("100,50"), 100.50)

    def test_clean_float_with_currency_sign(self):
        """Verify currency signals are stripped accurately."""
        self.assertEqual(BillValidator.clean_and_validate_float("$45.50"), 45.50)

    def test_validate_people_fails_on_decimal(self):
        """Verify strict whole-number enforcement triggers ValueError."""
        with self.assertRaises(ValueError):
            BillValidator.validate_people("9.4")


class TestBillSplitterService(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_receipts.txt"
        self.service = BillSplitterService(filename=self.test_file)

    def tearDown(self):
        """Cleanup IO artifacts post testing."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_math_determinism(self):
        """Verify standard split math returns precise limits."""
        total, per_person = BillSplitterService.calculate(100.0, 10.0, 2)
        self.assertEqual(total, 110.0)
        self.assertEqual(per_person, 55.0)

    def test_zero_division_guard(self):
        """Verify edge case system safety guards."""
        with self.assertRaises(ZeroDivisionError):
            BillSplitterService.calculate(100.0, 15.0, 0)


if __name__ == "__main__":
    unittest.main()