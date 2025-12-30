"""
step9に関連するコードを掲載
"""
from step6_7_8 import *

def square(x):
    f = Square()
    return f(x)
def exp(x):
    f = Exp()
    return f(x)

# 動作テスト
x = Variable(np.array([0.5]))
a = square(x)
b = exp(a)
c = square(b)
c.grad = np.array(1.0)
c.backward()
print(x.grad)

y = square(exp(square(x)))
y.grad = np.array(1.0)
y.backward()

print(x.grad)
x = np.array([0.5])
y = x ** 2
print(type(x), x.ndim)
print(type(y))
print(np.isscalar(1.0))
