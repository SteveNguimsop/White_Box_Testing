
import unittest
from Leap_Year import Leap_Year

# These tests achieve 100% branch and condition coverage.
# The entire decision produces both True and False,
# and conditions A, B, and C each evaluate both ways.
#
# However, this is NOT 100% MC/DC.
# Condition B is not shown to independently change
# the overall decision while A and C remain fixed.
# An additional test using 1900 would demonstrate this.


class Branch_And_Condition_Coverage_Tests(unittest.TestCase):

    def test_regular_year(self):
        self.assertFalse(Leap_Year(2023))

    def test_regular_leap_year(self):
        self.assertTrue(Leap_Year(2024))

    def test_century_leap_year(self):
        self.assertTrue(Leap_Year(2000))


if __name__ == "__main__":
    unittest.main()
