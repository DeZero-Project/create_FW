import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
import numpy as np
from example.stage2.stage2 import Variable

class TestVariable(unittest.TestCase):
    def test_init(self):
        data = np.array(1.0)
        v = Variable(data, name='v')
        self.assertEqual(v.data, 1.0)
        self.assertEqual(v.name, 'v')

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            Variable([1, 2, 3])

    def test_clearngrad(self):
        v = Variable(np.array(1.0))
        v.grad = np.array(1.0)
        v.crearngrad()
        self.assertIsNone(v.grad)
    
    def test_shape(self):
        data = np.array([[10, 20, 3],[4, 5, 6]])
        v = Variable(data)
        self.assertEqual(v.shape, (2,3))
    
    def test_ndim(self):
        data = np.array([[10, 20, 3],[4, 5, 6]])
        v = Variable(data)
        self.assertEqual(v.ndim, 2)

    def test_dtype(self):
        data = np.array([[10, 20, 3],[4, 5, 6]])
        v = Variable(data)
        self.assertEqual(v.dtype, data.dtype)

    def test_size(self):
        data = np.array([[10, 20, 3],[4, 5, 6]])
        v = Variable(data)
        self.assertEqual(v.size, data.size)
    
    def test_len(self):
        v = Variable(np.zeros((5, 20)))
        self.assertEqual(len(v),5)

    def test_repr(self):
        v = Variable(np.array([10,20]))
        self.assertEqual(str(v), 'Variable([10 20])')

    def test_add_forward(self):
        x0 = Variable(np.array(3.0))
        x1 = Variable(np.array(2.0))
        y = x0 + x1
        self.assertEqual(y.data, 5.0)

    def test_mul_forward(self):
        x0 = Variable(np.array(3.0))
        x1 = Variable(np.array(2.0))
        y = x0 * x1
        self.assertEqual(y.data, 6.0)

    def test_add_backward(self):
        x0 = Variable(np.array(3.0))
        x1 = Variable(np.array(2.0))
        y = x0 + x1
        y.backward()
        self.assertEqual(x0.grad, 1.0)
        self.assertEqual(x1.grad, 1.0)

    def test_mul_backward(self):
        x0 = Variable(np.array(3.0))
        x1 = Variable(np.array(2.0))
        y = x0 * x1
        y.backward()
        self.assertEqual(x0.grad, 2.0)
        self.assertEqual(x1.grad, 3.0)

    def test_add_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(3.0))
            x0 + 'a'

    def test_mul_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(3.0))
            x0 * 'a'

    def test_radd(self):
        x = Variable(np.array(2.0))
        y = 3.0 + x
        self.assertEqual(y.data, 5.0)

    def test_rmul(self):
        x = Variable(np.array(3.0))
        y = 3.0 * x
        self.assertEqual(y.data, 9.0)

    def test_radd_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(3.0))
            'a'+ x0

    def test_rmul_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(3.0))
            'a' * x0
    
    def test_sub(self):
        x = Variable(np.array(5.0))
        y = x - 3.0
        self.assertEqual(y.data, 2.0)

    def test_rsub(self):
        x = Variable(np.array(3.0))
        y = 5.0 - x
        self.assertEqual(y.data, 2.0)

    def test_div(self):
        x = Variable(np.array(6.0))
        y = x / 3.0
        self.assertEqual(y.data, 2.0)

    def test_rdiv(self):
        x = Variable(np.array(3.0))
        y = 6.0 / x
        self.assertEqual(y.data, 2.0)

    def test_pow(self):
        x = Variable(np.array(2.0))
        y = x ** 2
        self.assertEqual(y.data, 4.0)

    def test_neg(self):
        x = Variable(np.array(3.0))
        y = -x
        self.assertEqual(y.data, -3.0)

    def test_sub_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(3.0))
            'a'- x0

    def test_div_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(3.0))
            'a' / x0

    def test_pow_error(self):
        with self.assertRaises(TypeError):
            x0 = Variable(np.array(3.0))
            x0 ** 'a'

    def test_neg_error(self):
        with self.assertRaises(TypeError):
            -'a' 
    
if __name__ == '__main__':
    unittest.main()