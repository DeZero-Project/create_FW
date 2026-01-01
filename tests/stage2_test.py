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
if __name__ == '__main__':
    unittest.main()