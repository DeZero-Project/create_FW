import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from dezero.core_simple import *
from dezero.test_function import *
import contextlib
from dezero.util import *

x = Variable(np.array(np.pi / 4))
y = sin(x)
y.backward()
print(y.data)
print(x.grad)

plot_dot_graph(y, to_file='sin_graph.png')