import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import numpy as np
import dezero as F

np.random.seed(0)
x = np.random.randn(100, 1)
y = 5 + 2 * x + np.random.randn(100, 1)

W = F.Variable(np.zeros(1, 1))
b = F.Variable(np.zeros(1))

