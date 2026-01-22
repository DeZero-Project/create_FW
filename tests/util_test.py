"""
utilクラスのテスト
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from dezero.core_simple import *
from dezero.util import plot_dot_graph
from dezero.test_function import *

import numpy as np
class TestUtil(unittest.TestCase):
    def test_graphviz(self):
        x0 = Variable(np.array(1.0))
        x1 = Variable(np.array(1.0))

        y = matyas(x0, x1)
        tmp_file = "/app/docs/images/test_graph.png"
        plot_dot_graph(y, to_file="test_graph.png")

        self.assertTrue(os.path.exists(tmp_file))
        if os.path.exists(tmp_file): os.remove(tmp_file)

    def test_graph_size(self):
        x0 = Variable(np.array(1.0))
        x1 = Variable(np.array(1.0))

        y = matyas(x0, x1)
        tmp_file = "/app/docs/images/test_graph.png"
        plot_dot_graph(y, to_file="test_graph.png")

        self.assertGreater(os.path.getsize(tmp_file), 0)
        if os.path.exists(tmp_file): os.remove(tmp_file)

    def test_graphviz_error(self):
        with self.assertRaises(FileNotFoundError):

            x0 = Variable(np.array(1.0))
            x1 = Variable(np.array(1.0))

            y = matyas(x0, x1)
            tmp_file = "/app/docs/images/test_graph.png"
            plot_dot_graph(y, to_file=tmp_file)
            os.remove(tmp_file)

    def test_graph_size_error(self):
        with self.assertRaises(AssertionError):

            x0 = Variable(np.array(1.0))
            x1 = Variable(np.array(1.0))
            y = matyas(x0, x1)
            tmp_file = "/app/docs/images/test_graph.png"
            plot_dot_graph(y, to_file="test_graph.png")
            self.assertGreater(0, os.path.getsize(tmp_file))

if __name__ == '__main__':
    unittest.main()