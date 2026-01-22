import numpy as np
from dezero.core_simple import *

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
