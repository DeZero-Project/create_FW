"""
step3関連のコードを掲載
"""
import numpy as np
from step1 import Variable
from step2 import Function,Square

class Exp(Function):
    """
    引数にネイピア数をかける関数
    """
    def forward(self, x):
        return np.exp(x)
    
# 動作確認
x = Variable(np.array(1.5))
e = Exp()
s = Square()
s2 = Square()
s = s(x)
e = e(s)
s2 = s2(e)
print(s.data)