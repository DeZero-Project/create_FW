import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from dezero.core_simple import *
from dezero.test_function import *
import contextlib
from dezero.util import *

x0 = Variable(np.array(0.0))
x1 = Variable(np.array(0.0))
lr = 0.001
iters = 50000
for i in range(iters):
    print(x0, x1)

    z = rosenbrock(x0, x1)

    x0.crearngrad()
    x1.crearngrad()
    z.backward()

    x0.data -= lr * x0.grad
    x1.data -= lr * x1.grad

plot_dot_graph(z, to_file='rosenbrock.png')