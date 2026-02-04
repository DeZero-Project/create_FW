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

    def setUp(self):
        self.x_data = np.array([[1, 2, 3], [4, 5, 6]])
        self.x = Variable(self.x_data)

    def test_sum_forward(self):
        y = sum(self.x)
        expected = np.sum(self.x_data)
        self.assertTrue(np.allclose(y.data, expected))

        y_axis = sum(self.x, axis=0)
        expected_axis = np.sum(self.x_data, axis=0)
        self.assertTrue(np.allclose(y_axis.data, expected_axis))

    def test_sum_backward(self):
        y = sum(self.x, axis=1, keepdims=True)
        y.backward()

        expected_gx = np.ones_like(self.x_data)
        self.assertTrue(np.allclose(self.x.grad.data, expected_gx))

    def test_broadcast_to_forward(self):
        shape = (2, 3)
        x_small = Variable(np.array([1, 2, 3]))
        y = broadcast_to(x_small, shape)
        
        expected = np.broadcast_to(x_small.data, shape)
        self.assertEqual(y.shape, shape)
        self.assertTrue(np.allclose(y.data, expected))

    def test_broadcast_to_backward(self):
        x_small = Variable(np.array([1, 2, 3]))
        y = broadcast_to(x_small, (2, 3))
        y.backward()

        expected_gx = np.array([2, 2, 2])
        self.assertTrue(np.allclose(x_small.grad.data, expected_gx))

    def test_sum_to_forward(self):
        shape = (1, 3)
        y = sum_to(self.x, shape)

        expected = self.x_data.sum(axis=0, keepdims=True)
        self.assertTrue(np.allclose(y.data, expected))

    def test_sum_to_backward(self):
        shape = (1, 3)
        y = sum_to(self.x, shape)
        y.backward()
        
        expected_gx = np.ones_like(self.x_data)
        self.assertTrue(np.allclose(self.x.grad.data, expected_gx))

if __name__ == '__main__':
    unittest.main()