import cupy as np
from stage2 import *
import weakref

# 動作実験
for i in range(10):
    x = Variable(np.random.randn(4000))
    y = square(square(square(x)))
print(y)
w_ref =  weakref.ref(y)
y = None
if w_ref() is None:
    print("メモリの開放を確認")
    print(w_ref())
else:
    print("メモリが破棄されていません")
    print(w_ref())