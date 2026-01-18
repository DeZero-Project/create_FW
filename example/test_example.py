import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from dezero.core_simple import *
from dezero.test_function import *
import contextlib
from dezero.util import *

x0 = Variable(np.array(2.0))

y = f(x0)
y.backward(create_graph=True)
print(x0.grad)

gx = x0.grad
x0.crearngrad()
gx.backward()
print(x0.grad.data)