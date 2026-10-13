
import unittest
from Leap_Year import Leap_Year

# These 8 tests achieve 100% feasible
# multiple conditions coverage (MCC).
#
# D = year % 7 == 0
# A = year % 4 == 0
# B = year % 100 != 0
# C = year % 400 == 0
#
# Only 8 of the 16 theoretical combinations
# are possible for integer years.
# These tests cover all 8 feasible combinations.


class Multiple_Conditions_Coverage_Tests(unittest.TestCase):

    def test_2023(self):
        # D=True, A=False, B=True, C=False
        self.assertFalse(Leap_Year(2023))

    def test_2016(self):
        # D=True, A=True, B=True, C=False
        self.assertTrue(Leap_Year(2016))

    def test_2100(self):
        # D=True, A=True, B=False, C=False
        self.assertFalse(Leap_Year(2100))

    def test_2800(self):
        # D=True, A=True, B=False, C=True
        self.assertTrue(Leap_Year(2800))

    def test_2025(self):
        # D=False, A=False, B=True, C=False
        self.assertFalse(Leap_Year(2025))

    def test_2024(self):
        # D=False, A=True, B=True, C=False
        self.assertTrue(Leap_Year(2024))

    def test_1900(self):
        # D=False, A=True, B=False, C=False
        self.assertFalse(Leap_Year(1900))

    def test_2000(self):
        # D=False, A=True, B=False, C=True
        self.assertTrue(Leap_Year(2000))


if __name__ == "__main__":
    unittest.main()
