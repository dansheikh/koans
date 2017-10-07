import unittest
import trees.algorithms


class TestTrees(unittest.TestCase):

    def test_build_graph(self):
        test_seq1 = [1, 2, 3]
        test_seq2 = [3, 1, 2]
        test_seq3 = list(range(10))

        graph1 = trees.algorithms.build_graph(test_seq1)
        graph2 = trees.algorithms.build_graph(test_seq2)
        graph3 = trees.algorithms.build_graph(test_seq3)

        self.assertEqual(2, graph1.root.val)
        self.assertEqual(2, graph2.root.val)
        self.assertEqual(2, graph3.root.val)
