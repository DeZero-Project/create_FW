import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
import numpy as np
import dezero as F

class test_reshape(unittest.TestCase):
    def test_N01(self):
        x = F.Variable(np.array([[2, 3], [4, 5], [6, 7]]))
        y = x.reshape(x.shape)
        self.assertEqual((3, 2),y.shape)

    def test_N02(self):
        x = F.Variable(np.array([[2, 3], [4, 5], [6, 7]]))
        y = x.transpose((0, 1))
        self.assertEqual((3, 2),y.shape)

    def test_N03(self):
        x = F.Variable(np.array([[2, 3], [4, 5], [6, 7]]))
        shape = (-1,)
        y = x.reshape(shape)
        self.assertEqual((6,),y.shape)

    def test_N04(self):
        x = F.Variable(np.array([[2, 3], [4, 5], [6, 7]]))
        x0 = x.reshape(2, 3)
        y = F.sin(x0)
        y.backward(create_graph=True) 
        self.assertEqual(x.grad.shape, (3, 2))

    def test_N05(self):
        x = F.Variable(np.array([[2, 3], [4, 5], [6, 7]]))
        x0 = x.transpose(1, 0)
        y = F.sin(x0)
        y.backward(create_graph=True)
        self.assertEqual(x.grad.shape, (3, 2))

    def test_E01(self):
        with self.assertRaises(ValueError):
            x = F.Variable(np.array([[2, 3], [4, 5], [6, 7]]))
            x.reshape(5, 0)
        
    def test_E02(self):
        with self.assertRaises(ValueError):
            x = F.Variable(np.array([[2, 3], [4, 5], [6, 7]]))
            x.transpose(3, 2)
        

if __name__ == '__main__':
    unittest.main()