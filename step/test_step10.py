"""
step10に関するコード(テスト関連)を掲載
"""
from step6_7_8 import *
from step4 import numerical_diff
from step9 import *
import unittest
import numpy as np


class SquareTest(unittest.TestCase):
    def test_forward(self):
        x = Variable(np.array(2.0))
        y = square(x)
        excepted = np.array(4.0)
        self.assertEquals(y.data, excepted)
    def test_backward(self):
        x = Variable(np.random.randn(1))
        y = square(x)
        y.backward()
        num_grad = numerical_diff(square, x)
        flg = np.allclose(x.grad, num_grad)
        self.assertTrue(flg)

class ExpTest(unittest.TestCase):
    def test_forward(self):
        x = Variable(np.array(2.0))
        y = exp(x)
        excepted = np.exp(2.0)
        self.assertEquals(y.data, excepted)
    def test_backward(self):
        x = Variable(np.random.randn(1))
        y = exp(x)
        y.backward()
        num_grad = numerical_diff(exp, x)
        flg = np.allclose(x.grad, num_grad)
        self.assertTrue(flg)
unittest.main()