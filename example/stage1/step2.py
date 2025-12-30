"""
Step2に関連するコードを掲載
"""
import numpy as np
from step1 import Variable
class Function:
    """
    関数の基底クラス定義
    """
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        out = Variable(y)
        return out
    def forward(self, x):
        raise NotImplementedError
    
class Square(Function):
    """
    引数を2乗する関数
    """
    def forward(self, x):
        return x ** 2
    
# 動作確認    
x = Variable(np.ndarray([5, 7]))
y = Square()
y = y(x)
print(y.data)