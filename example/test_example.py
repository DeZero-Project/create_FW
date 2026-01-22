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
x0.name = "x"
y.name = "y"
print(y.data)
y.backward(create_graph=True)

iters = 4
for i in range(iters):
    gx = x0.grad
    x0.crearngrad()
    gx.backward(create_graph=True)

gx = x0.grad
gx.name = "gx" + str(iters + 5)
plot_dot_graph(gx,verbose=False, to_file='tanh.png')