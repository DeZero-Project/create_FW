import cupy as np
from stage2 import *

# 動作実験
x1 = Variable(np.array(3))
x0 = Variable(np.array(15))
ys = add(square(x0), square(x1))
ys.backward()
print(ys.data)
print(x0.grad, x1.grad)

x = Variable(np.array(3.0))
y = add(x, x)
y.backward()
print(x.grad)

x.creargrad()
y = add(add(x, x), x)
y.backward()
print(x.grad)
print(ys.generation)

x = Variable(np.array(2.0))
a = square(x)
y = add(square(a), square(a))
y.backward()
print(y.data)
print(x.grad)