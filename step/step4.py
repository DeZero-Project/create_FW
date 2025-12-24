"""
step4に関連のコードを掲載
"""
from step1 import Variable
from step2 import *
from step3 import Exp
import numpy as np

def numerical_diff(f, x, eps=1e-4):
    """
    :param f: インスタンス化した関数
    :param x: 微分を求める変数
    :param eps: 0除算防止用定数
    """
    x0 = Variable(x.data + eps)
    x1 = Variable(x.data - eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y0.data - y1.data) / (2 * eps)

def func(x):
    s = Square()
    e = Exp()
    s2 = Square()
    s = s(x)
    e = e(s)
    s2 = e
    return s2

# 動作確認
x = Variable(np.array(10))
dx = numerical_diff(func, x)
print(dx)
