import unittest

from src.lab5 import min_beers


class TestMinBeersFunction(unittest.TestCase):

    def test_two_employees_which_like_different_beers(self):
        num_employees = 2
        num_beers = 2
        preferences = "YN NY"
        result = min_beers(num_employees, num_beers, preferences)
        self.assertEqual(result, 2)

    def test_extra_beer(self):
        num_employees = 6
        num_beers = 3
        preferences = "YNN YNY YNY NYY NYY NYN"
        result = min_beers(num_employees, num_beers, preferences)
        self.assertEqual(result, 2)

    def test_min_beers_invalid_num_employees(self):
        num_employees = 55
        num_beers = 4
        preferences = "YNNY NYNY YYYN"
        result = min_beers(num_employees, num_beers, preferences)
        self.assertEqual(result, -1)

    def test_min_beers_invalid_num_beers(self):
        num_employees = 3
        num_beers = 60
        preferences = "YNN NYN YYN"
        result = min_beers(num_employees, num_beers, preferences)
        self.assertEqual(result, -1)

    def test_min_beers_invalid_preferences_length(self):
        num_employees = 3
        num_beers = 4
        preferences = "YNNY NYNY YNYYY"
        result = min_beers(num_employees, num_beers, preferences)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
