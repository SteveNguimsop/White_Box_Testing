
import unittest
from Leap_Year import Leap_Year

# These tests achieve 100% condition coverage because
# all individual conditions evaluate to both True and False.
# However, they do not achieve 100% statement coverage
# or branch coverage because the return statement in
# the else block is not executed.


class Condition_Coverage_Tests(unittest.TestCase):

    def test_regular_year(self):
        self.assertFalse(Leap_Year(2023))

    def test_century_not_leap(self):
        self.assertFalse(Leap_Year(1900))

    def test_century_leap(self):
        self.assertTrue(Leap_Year(2000))


if __name__ == "__main__":
    unittest.main()
