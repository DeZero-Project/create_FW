import numpy as np
from dezero.core_simple import *
from dezero import util
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
    
class Sin(Function):
    def forward(self, x):
        y = np.sin(x)
        return y
    def backward(self, gy):
        x = self.inputs[0]
        gx = gy * cos(x)
        return gx
    
class Cos(Function):
    def forward(self, x):
        y = np.cos(x)
        return y
    def backward(self, gy):
        x = self.inputs[0]
        gx = gy * -sin(x)
        return gx
    
class Tanh(Function):
    def forward(self, x):
        y = np.tanh(x)
        return y
    def backward(self, gy):
        x = self.outputs[0]()
        gx = gy * (1 - x**2)
        return gx
    
def square(x):
    f = Square()
    return f(x)
def exp(x):
    f = Exp()

def sin(x):
    return Sin()(x)
def cos(x):
    return Cos()(x)
def tanh(x):
    return Tanh()(x)

class Reshape(Function):
    def __init__(self, shape):
        self.shape = shape
    
    def forward(self, x):
        self.x_shape = x.shape
        y = x.reshape(self.shape)
        return y
    
    def backward(self, gy):
        return reshape(gy, self.x_shape)
    
def reshape(x, shape):
    if x.shape == shape:
        return as_variable(x)
    return Reshape(shape)(x)

class Transpose(Function):
    def __init__(self, axes=None):
        self.axes = axes
    def forward(self, x):
        y = x.transpose(self.axes)
        return y
    def backward(self, gy):
        if self.axes is None:
            return transpose(gy)
        axes_len = len(self.axes)
        inv_axes = tuple(np.argsort([ax % axes_len for ax in self.axes]))
        return transpose(gy, inv_axes)

def transpose(x, axes=None):
    return Transpose(axes)(x)

class Sum(Function):
    def __init__(self, axis, keepdims):
        self.axis = axis
        self.keepdims = keepdims
    def forward(self, x):
        self.x_shape = x.shape
        y = x.sum(axis = self.axis, keepdims = self.keepdims)

        return y
    def backward(self, gy):
        gy = util.reshape_sum_backward(gy,self.x_shape ,self.axis, self.keepdims)
        gx = broadcast_to(gy, self.x_shape)
        return gx
def sum(x, axis = None, keepdims = False):
    return Sum(axis=axis, keepdims=keepdims)(x)

class BroadcastTo(Function):
    def __init__(self, shape):
        self.shape = shape
    
    def forward(self, x):
        self.x_shape = x.shape
        y = np.broadcast_to(x, self.shape)
        return y
    
    def backward(self, gy):
        gx = sum_to(gy, self.x_shape)
        return gx
    
def broadcast_to(x, shape):
    if x.shape == shape:
       return as_variable(x)
    return BroadcastTo(shape)(x)

class SumTo(Function):
    def __init__(self, shape):
        self.shape = shape
    
    def forward(self, x):
        self.x_shape = x.shape
        y = util.sum_to(x, self.shape)
        return y
    
    def backward(self, gy):
        gx = broadcast_to(gy, self.x_shape)
        return gx
    
def sum_to(x, shape):
    if x.shape == shape:
       return as_variable(x)
    return SumTo(shape)(x)

