import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
import numpy as np
from dezero.core_simple import *
from dezero.function import *
from dezero.util import numerical_diff
class TestSin(unittest.TestCase):
    def test_N01(self):
        x = Variable(np.array(2.0))
        y = sin(x)
        self.assertTrue(np.allclose(y.data, np.sin(x.data)))

    def test_E01(self):
        with self.assertRaises(TypeError):
            sin('a')

class TestFunctions(unittest.TestCase):
    def test_n01(self):
        x = Variable(np.array([2.0]))
        y = sin(as_array(x))
        y.backward()
        exp = np.allclose(x.grad.data, numerical_diff(sin, x), atol=1e-8)
        self.assertTrue(exp)
    
    def test_n02(self):
        x = Variable(np.array([2.0]))
        y = cos(as_array(x))
        y.backward()
        exp = np.allclose(x.grad.data, numerical_diff(cos, x), atol=1e-8)
        self.assertTrue(exp)

    def test_n03(self):
        x = Variable(np.array([2.0]))
        y = tanh(as_array(x))
        y.backward()
        exp = np.allclose(x.grad.data, numerical_diff(tanh, x), atol=1e-8)
        self.assertTrue(exp)

    def test_E01(self):
        with self.assertRaises(TypeError):
            sin('a')

    def test_E02(self):
        with self.assertRaises(TypeError):
            cos('a')

    def test_E03(self):
        with self.assertRaises(TypeError):
            tanh('a')


if __name__ == '__main__':
    unittest.main()