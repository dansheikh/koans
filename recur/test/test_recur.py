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
