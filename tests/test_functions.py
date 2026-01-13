import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
import numpy as np
from dezero.core_simple import *
from dezero.test_function import *

class TestSin(unittest.TestCase):
    def test_N01(self):
        x = Variable(np.array(2.0))
        y = sin(x)
        self.assertTrue(np.allclose(y.data, np.sin(x.data)))

    def test_E01(self):
        with self.assertRaises(TypeError):
            sin('a')
            
if __name__ == '__main__':
    unittest.main()