import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from dezero.core_simple import *
from dezero.test_function import *
import contextlib
from dezero.util import *
from dezero.function import *

x0 = Variable(np.array(2.0))

y = tanh(x0)
print(y.data)
y.backward(create_graph=True)

for i in range(3):
    gx = x0.grad
    x0.crearngrad()
    gx.backward(create_graph=True)
    print(x0.grad)