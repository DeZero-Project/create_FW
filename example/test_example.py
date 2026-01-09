import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from dezero.core_simple import *
from dezero.test_function import *
import contextlib
from dezero.util import *
x0 = Variable(np.array(1.0))
x1 = Variable(np.array(1.0))

z = matyas(x0, x1)
z.backward()

x0.name = 'x0'
x1.name = 'x1'
z.name = 'z'
plot_dot_graph(z, verbose=False, to_file='matyas.png')