import unittest
import sorts.algorithms


class TestSorts(unittest.TestCase):

    def test_quicksort(self):
        test_seq5 = [3, 1, 0, 4, 2]
        test_seq10 = [9, 7, 3, 1, 0, 6, 2, 8, 4, 5]

        sorts.algorithms.quicksort(test_seq5)
        sorts.algorithms.quicksort(test_seq10)

        self.assertEqual([0, 1, 2, 3, 4], test_seq5)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], test_seq10)

    def test_mergesort(self):
        test_seq5 = [3, 1, 0, 4, 2]
        test_seq10 = [9, 7, 3, 1, 0, 6, 2, 8, 4, 5]

        sorts.algorithms.mergesort(test_seq5)
        sorts.algorithms.mergesort(test_seq10)

        self.assertEqual([0, 1, 2, 3, 4], test_seq5)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], test_seq10)
