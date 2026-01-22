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
<<<<<<< HEAD
        self.assertEqual(x0.grad, 2.0)
        self.assertEqual(x1.grad, 2.0)
=======
        self.assertEqual(x0.grad.data, 2.0)
        self.assertEqual(x1.grad.data, 2.0)
>>>>>>> stage3

    def test_matyas(self):
        x0 = Variable(np.array(1.0))
        x1 = Variable(np.array(1.0))
        z = matyas(x0, x1)
        z.backward()
<<<<<<< HEAD
        self.assertEqual(x0.grad, 0.040000000000000036)
        self.assertEqual(x1.grad, 0.040000000000000036)

    def test_matyas(self):
=======
        self.assertEqual(x0.grad.data, 0.040000000000000036)
        self.assertEqual(x1.grad.data, 0.040000000000000036)

    def test_goldstein_price(self):
>>>>>>> stage3
        x0 = Variable(np.array(1.0))
        x1 = Variable(np.array(1.0))
        z = goldstein_price(x0, x1)
        z.backward()
<<<<<<< HEAD
        self.assertEqual(x0.grad, -5376.0)
        self.assertEqual(x1.grad, 8064.0)
=======
        self.assertEqual(x0.grad.data, -5376.0)
        self.assertEqual(x1.grad.data, 8064.0)
>>>>>>> stage3

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
<<<<<<< HEAD

=======
    
    def test_rosenbrock_minimum(self):
        x0 = Variable(np.array(1.0))
        x1 = Variable(np.array(1.0))
        z = rosenbrock(x0, x1)
        self.assertEqual(z.data, 0.0)

    def test_rosenbrock_origin(self):
        x0 = Variable(np.array(0.0))
        x1 = Variable(np.array(0.0))
        z = rosenbrock(x0, x1)
        z.backward()
        self.assertEqual(z.data, 1.0)
        self.assertEqual(x0.grad.data, -2.0)
    
    def test_rosenbrock_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(1.0))
            rosenbrock(x0, 'a')

    def test_rosenbrock_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(1.0))
            rosenbrock(x0, None)

    def test_higher_derivative(self):
        x = Variable(np.array(2.0))
        z = f(x)
        z.backward(create_graph=True)
        gx = x.grad
        x.crearngrad()
        gx.backward()
        self.assertEqual(x.grad.data, 44.0)
    
    def test_higher_derivative_error(self):
        with self.assertRaises(TypeError):
            x = Variable(np.array(1.0))
            z = f(None)
            z.backward(create_graph=True)
            gx = x.grad
            x.crearngrad()
            gx.backward()
>>>>>>> stage3

if __name__ == '__main__':
    unittest.main()