
import unittest
from Leap_Year import Leap_Year

# These tests achieve 100% statement coverage because
# every executable statement in Leap_Year.py is executed.
# However, they do not achieve 100% condition coverage
# because the condition (year % 100 == 0) is never False.


class Statement_Coverage_Tests(unittest.TestCase):

    def test_not_divisible_by_4(self):
        self.assertFalse(Leap_Year(2023))

    def test_century_not_leap_year(self):
        self.assertFalse(Leap_Year(1900))

    def test_century_leap_year(self):
        self.assertTrue(Leap_Year(2000))


if __name__ == "__main__":
    unittest.main()
