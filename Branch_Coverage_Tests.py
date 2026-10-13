
import unittest
from Leap_Year import Leap_Year

# These tests achieve 100% branch coverage because
# every decision takes both its True and False branches.
# However, they do not achieve 100% condition coverage
# because the second condition in the first "and"
# expression never evaluates to False.


class Branch_Coverage_Tests(unittest.TestCase):

    def test_regular_year(self):
        self.assertFalse(Leap_Year(2023))

    def test_regular_leap_year(self):
        self.assertTrue(Leap_Year(2024))

    def test_century_not_leap(self):
        self.assertFalse(Leap_Year(1900))

    def test_century_leap(self):
        self.assertTrue(Leap_Year(2000))


if __name__ == "__main__":
    unittest.main()
