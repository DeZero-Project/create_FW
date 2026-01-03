import cupy as np
from stage2 import *
import weakref

# 動作実験
x0 = Variable(np.array(5.0))

y =  5.0 * x0
print(y)