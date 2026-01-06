import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from dezero.core_simple import *
import contextlib

x0 = Variable(np.array(1.0), name='x')
print(x0.name)
print(x0.dtype)
print(x0.ndim)