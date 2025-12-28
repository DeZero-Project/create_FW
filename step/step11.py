"""
step11で行う改修型基底クラスの実装
"""
import numpy as np

class Variable:
    """
    Vriableクラスに与えられたデータの重みを取り出す仕様を追加
    """
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
               raise TypeError("{} is not supported".format(type(data)))
        self.data = data
        self.grad = None
        self.creator = None
    
    def set_creator(self, func):
        """
        対象の変数を作成した関数を保持する
        :param func: 対象の変数を作成した関数名
        """
        self.creator = func

    
    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            gys = [output.grad for output in f.outputs]
            gxs =  f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)
            for x, gx in zip(f.inputs, gxs):
                if x.grad is None:
                    x.grad = gx
                else:
                    x.grad = x.grad + gx
                if x.creator is not None:
                    funcs.append(x.creator)
    def creargrad(self):
        self.grad = None

class Function:
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(as_array(y))for y in ys]
        
        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs
        self.outputs = outputs

        return outputs if len(outputs) > 1 else outputs[0]
    
    def forward(self, xs):
        raise NotImplementedError()
    def backward(self, gys):
        raise NotImplementedError()


class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1
        return (y,)
    def backward(self, gy):
        return gy, gy


class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y
    
    def backward(self, gy):
        x = self.inputs[0].data
        gx = 2 * x * gy
        return gx

class Exp(Function):
    def forward(self, x):
        y = np.exp(x)
        return y
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx
def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x

def square(x):
    f = Square()
    return f(x)
def exp(x):
    f = Exp()
    return f(x)
def add(x0, x1):
    return Add()(x0, x1)




# 動作実験
x1 = Variable(np.array(3))
x0 = Variable(np.array(15))
ys = add(square(x0), square(x1))
ys.backward()
print(ys.data)
print(x0.grad, x1.grad)

x = Variable(np.array(3.0))
y = add(x, x)
y.backward()
print(x.grad)

x.creargrad()
y = add(add(x, x), x)
y.backward()
print(x.grad)