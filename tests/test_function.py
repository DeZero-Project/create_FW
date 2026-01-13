import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
import numpy as np
from dezero.core_simple import Variable
from dezero.test_function import *

class TestFunction(unittest.TestCase):
    def test_sphere(self):
        x0 = Variable(np.array(1.0))
        x1 = Variable(np.array(1.0))
        z = sphere(x0, x1)
        z.backward()
        self.assertEqual(x0.grad, 2.0)
        self.assertEqual(x1.grad, 2.0)

    def test_matyas(self):
        x0 = Variable(np.array(1.0))
        x1 = Variable(np.array(1.0))
        z = matyas(x0, x1)
        z.backward()
        self.assertEqual(x0.grad, 0.040000000000000036)
        self.assertEqual(x1.grad, 0.040000000000000036)

    def test_matyas(self):
        x0 = Variable(np.array(1.0))
        x1 = Variable(np.array(1.0))
        z = goldstein_price(x0, x1)
        z.backward()
        self.assertEqual(x0.grad, -5376.0)
        self.assertEqual(x1.grad, 8064.0)

    def test_sphere_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(1.0))
            sphere(x0, 'a')

    def test_matyas_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(1.0))
            matyas(x0, 'a')

    def test_goldstein_price_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(1.0))
            goldstein_price(x0, 'a')


if __name__ == '__main__':
    unittest.main()