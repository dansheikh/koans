import unittest
import search.algorithms


class TestSearch(unittest.TestCase):

    def test_min_diff_equal_len(self):
        test_alpha = [9, 28, 12, 1, 6]
        test_beta = [3, 5, 10, 33, 15]

        test_diff = search.algorithms.min_diff(test_alpha, test_beta)

        self.assertEqual(test_diff, 1)

    def test_min_diff_unequal_len(self):
        test_alpha = [9, 28, 12]
        test_beta = [3, 5, 33, 15]

        test_diff = search.algorithms.min_diff(test_alpha, test_beta)

        self.assertEqual(test_diff, 3)
