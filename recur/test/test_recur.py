import unittest
import recur.algorithms


class TestRecur(unittest.TestCase):

    def test_make_change1(self):
        test_amt = 10
        test_vals = [2]

        ways = recur.algorithms.make_change(test_amt, test_vals)

        self.assertEquals(1, ways)

    def test_make_change2(self):
        test_amt = 10
        test_vals = [2, 5]

        ways = recur.algorithms.make_change(test_amt, test_vals)

        self.assertEquals(2, ways)

    def test_find_combinations1(self):
        test_amt = 7
        test_vals = [1, 6, 8]

        combos = recur.algorithms.find_combinations(test_amt, test_vals)

        self.assertEqual([[1, 6], [1, 1, 1, 1, 1, 1, 1]], combos)

    def test_find_combinations2(self):
        test_amt = 7
        test_vals = [6, 8, 1]

        combos = recur.algorithms.find_combinations(test_amt, test_vals)

        self.assertEqual([[1, 6], [1, 1, 1, 1, 1, 1, 1]], combos)

    def test_find_combinations3(self):
        test_amt = 7
        test_vals = [6, 8]

        combos = recur.algorithms.find_combinations(test_amt, test_vals)

        self.assertEqual([], combos)
