"""
step6,7,8関連のコードを掲載
"""
import numpy as np

class Variable:
    """
    Vriableクラスに与えられたデータの重みを取り出す仕様を追加
    """
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
               raise TypeError("{} is not supported".format(type(data)))
        self.data = data
        self.grad = None
        self.creator = None
    
    def set_creator(self, func):
        """
        対象の変数を作成した関数を保持する
    
        :param func: 対象の変数を作成した関数名
        """
        self.creator = func

    
    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            x, y = f.input, f.out
            x.grad = f.backward(y.grad)

            if x.creator is not None:
                funcs.append(x.creator)

def as_array(x):
    if np.isscalar(x):
        return np.array(x)
        
    return x

class Function:
    """
    逆伝播に対応した基底クラス
    """
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        out = Variable(as_array(y))
        out.set_creator(self)
        self.input = input
        self.out = out

        return out

    def forward(self, x):
        """
         :param x: 入力値
        """
        return NotImplementedError
    def backward(self, gy):
        """
        :param gy: 前層からの勾配
        """
        return NotImplementedError

class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y
    
    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx

class Exp(Function):
    def forward(self, x):
        y = np.exp(x)
        return y
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx
    
"""# 動作確認
A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
c = C(b)
print(c.data)

c.grad = np.array(1.0)
b.grad = C.backward(c.grad)
a.grad = B.backward(b.grad)
x.grad = A.backward(a.grad)
print(x.grad)

# 変数と関数の繋がりが保持されているか確認
assert c.creator == C
assert c.creator.input == b
assert c.creator.input.creator == B
assert c.creator.input.creator.input == a
assert c.creator.input.creator.input.creator == A
assert c.creator.input.creator.input.creator.input == x
print(a.creator)

# リンク付きノードを利用した逆伝播実験
c.grad = np.array(1.0)
C = c.creator
b = C.input
b.grad = C.backward(c.grad)
print(c.grad, b.grad)
B = b.creator
a = B.input
a.grad = B.backward(b.grad)
print(c.grad, a.grad)
A = a.creator
x = A.input
x.grad = A.backward(a.grad)
print(c.grad, x.grad)

# 自動化バックプロパゲーション実験
A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)

y.grad = np.array(1.0)
y.backward()
print(x.grad)"""
