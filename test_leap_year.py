import unittest
import leap_year

class classTestLeapYear(unittest.TestCase):
    def test_leap_year_1(self):
        self.assertEqual(leap_year.check_year(420), "420 is a leap year")

    def test_leap_year_2(self):
        self.assertEqual(leap_year.check_year(69), "69 is not a leap year")

    def test_leap_year_fail(self):
        self.assertEqual(leap_year.check_year(2020), "2020 is not a leap year")