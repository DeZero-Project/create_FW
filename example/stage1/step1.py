"""
step1関連のソースコードを掲載
"""
import numpy as np
class Variable:
    """
    変数定義用のクラス
    """
    def __init__(self, data):
        self.data = data

# Variableクラスの動作確認
data = np.ndarray([10,5,4])
x = Variable(data)
print(x.data.shape)
print(x.data.ndim)