"""
cupy未対応のコアロジック
"""
import numpy as np
import heapq
import weakref
import contextlib

class Variable:
    __array_prority__ = 200

    def __init__(self, data, name=None):
        if data is not None:
            if not isinstance(data, np.ndarray):
               raise TypeError("{} is not supported".format(type(data)))
        self.data = data
        self.grad = None
        self.creator = None
        self.name = name
        self.generation = 0

    def __len__(self): 
        return len(self.data)
    
    def __repr__(self):
        if self.data is None:
            return 'Valiable(None)'
        p = str(self.data).replace('\n', '\n' + '' * 9)
        return 'Variable(' + p + ')'
    
    def __mul__(self, other):
        return mul(self, other)
    
    def __add__(self, other):
        return add(self, other)
    
    def __rmul__(self, other):
        return mul(self, other)
    
    def __radd__(self, other):
        return add(self, other)
    
    def __sub__(self, other):
        return sub(self, other)
    
    def __rsub__(self, other):
        return rsub(self, other)
    
    def __truediv__(self, other):
        return div(self, other)
    
    def __rtruediv__(self, other):
        return rdiv(self, other)
    
    def __neg__(self):
        return neg(self)
    
    def __pow__(self, other):
        return pow(self, other)
    
    def set_creator(self, func):
        """
        対象の変数を作成した関数を保持する
        :param func: 対象の変数を作成した関数名
        """
        self.creator = func
        self.generation = func.generation + 1
    
    def backward(self, retain_grad=False):
        if self.grad is None:
            self.grad = np.ones_like(self.data)
        funcs = []
        seen_set = set()
        def add_func(f):
            if f not in seen_set:
                heapq.heappush(funcs, (-f.generation, id(f), f))
                seen_set.add(f)
        add_func(self.creator)
        while funcs:
            gen, _id, f = heapq.heappop(funcs)
            gys = [output().grad for output in f.outputs]
            gxs =  f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)
            for x, gx in zip(f.inputs, gxs):
                if x.grad is None:
                    x.grad = gx
                else:
                    x.grad = x.grad + gx
                if x.creator is not None:
                    add_func(x.creator)
            if not retain_grad:
                for y in f.outputs:
                    y().grad = None
    def crearngrad(self):
        self.grad = None
    
    @property
    def shape(self):
        return self.data.shape
    @property
    def ndim(self):
        return self.data.ndim
    @property
    def dtype(self):
        return self.data.dtype
    @property
    def size(self):
        return self.data.size
    
class Function(object):
    def __call__(self, *inputs):
        inputs = [as_variable(x) for x in inputs]
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(as_array(y))for y in ys]

        if Config.enabled_backprop:
            self.generation = max([x.generation for x in inputs])
            for output in outputs:
                output.set_creator(self)
            self.inputs = inputs
            self.outputs = [weakref.ref(output)for output in outputs]

        return outputs if len(outputs) > 1 else outputs[0]
    
    def forward(self, xs):
        raise NotImplementedError()
    def backward(self, gys):
        raise NotImplementedError()

class Neg(Function):
    def forward(self,x):
        return -x
    def backward(self, gy):
        return -gy
    
class Pow(Function):
    def __init__(self, c):
        self.c = c
    def forward(self,x):
        y = x ** self.c
        return y
    def backward(self, gy):
        x = self.inputs[0].data
        c = self.c
        gx = c * x ** (c - 1) * gy
        return gx

class Div(Function):
    def forward(self, x0,x1):
        y = x0 / x1
        return y
    def backward(self, gy):
        x0, x1 = self.inputs[0].data, self.inputs[1].data
        gx0 = gy / x0
        gx1 = gy * (-x0 / x1 ** 2)
        return gx0, gx1

class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1
        return (y,)
    def backward(self, gy):
        return gy, gy

class Sub(Function):
    def forward(self, x0, x1):
        y = x0 - x1
        return y
    def backward(self, gy):
        return gy, -gy

class Mul(Function):
    def forward(self, x0,x1):
        y = x0 * x1
        return y
    def backward(self, gy):
        x0, x1 = self.inputs[0].data, self.inputs[1].data
        return gy * x1, gy * x0


class Config:
    enabled_backprop = True

def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x
def as_variable(x):
    if isinstance(x, Variable):
        return x
    return Variable(x)


    return f(x)
def add(x0, x1):
    x1 = as_array(x1)
    return Add()(x0, x1)
def mul(x0, x1):
    x1 = as_array(x1)
    return Mul()(x0, x1)
def div(x0, x1):
    x1 = as_array(x1)
    return Div()(x0, x1)
def sub(x0, x1):
    x1 = as_array(x1)
    return Sub()(x0, x1)
def pow(x, c):
    return Pow(c)(x)
def rdiv(x0, x1):
    x1 = as_array(x1)
    return Div()(x1, x0)
def rsub(x0, x1):
    x1 = as_array(x1)
    return Sub()(x1, x0)
def neg(x):
    return Neg()(x)
@contextlib.contextmanager
def using_config(name, value):
    old_value = getattr(Config, name)
    setattr(Config, name, value)
    try:
        yield
    finally:
        setattr(Config, name, old_value)

def no_grad():
    return using_config('enabled_backprop', False)