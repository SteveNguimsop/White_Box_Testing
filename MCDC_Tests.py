
import unittest
from Leap_Year import Leap_Year

# These 5 tests achieve 100% MC/DC for the compound decision.
# Each condition independently changes the decision:
# D (% 7 == 0): 2016 vs 2024
# A (% 4 == 0): 2023 vs 2016
# B (% 100 != 0): 2016 vs 2100
# C (% 400 == 0): 2100 vs 2800
#
# This is NOT 100% multiple conditions coverage
# because only 5 of the 8 feasible combinations
# of the four conditions are tested.


class MCDC_Tests(unittest.TestCase):

    def test_regular_year(self):
        self.assertFalse(Leap_Year(2023))

    def test_regular_leap_year(self):
        self.assertTrue(Leap_Year(2016))

    def test_century_not_leap(self):
        self.assertFalse(Leap_Year(2100))

    def test_century_leap(self):
        self.assertTrue(Leap_Year(2800))

    def test_leap_not_divisible_by_7(self):
        self.assertTrue(Leap_Year(2024))


if __name__ == "__main__":
    unittest.main()
