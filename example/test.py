import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from example.stage2.stage2 import *
import contextlib

x0 = Variable(np.array(1.0))
x1 = Variable(np.array(2.0))
t = add(x0, x1)
y = add(x0, t)
y.backward()
print(x0.grad, x1.grad)


x = Variable(np.array(1.0))
y = square(x)
y.backward()
print(x.grad)

with no_grad():
    x = Variable(np.array(1.0))
    y = square(x)
    print(y.grad)