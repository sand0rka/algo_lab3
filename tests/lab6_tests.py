import unittest
from src.lab6 import knuth_morris_pratt


class TestNeedleSearch(unittest.TestCase):

    def test_empty_strings(self):
        result = knuth_morris_pratt("", "")
        self.assertEqual(result, [])

    def test_empty_needle(self):
        result = knuth_morris_pratt("abc", "")
        self.assertEqual(result, [])

    def test_empty_haystack(self):
        result = knuth_morris_pratt("", "needle")
        self.assertEqual(result, [])

    def test_single_occurrence(self):
        result = knuth_morris_pratt("ababcababcabc", "abc")
        self.assertEqual(result, [2, 7, 10])

    def test_multiple_occurrences(self):
        result = knuth_morris_pratt("abababab", "aba")
        self.assertEqual(result, [0, 2, 4])

    def test_no_occurrence(self):
        result = knuth_morris_pratt("abcdef", "xyz")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
