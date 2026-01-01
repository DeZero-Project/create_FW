"""
stage2で使用するクラス群
"""
import numpy as np
import heapq
import weakref
import contextlib
class Variable:
    """
    Vriableクラスに与えられたデータの重みを取り出す仕様を追加
    """
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

class Config:
    enabled_backprop = True

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