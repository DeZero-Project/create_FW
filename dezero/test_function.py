"""
最適化問題用テスト関数
"""
def sphere(x, y):
    z = x**2 + y**2
    return z

def matyas(x, y):
    z = 0.26 * (x**2 + y**2) - 0.48 * x * y
    return z

def goldstein_price(x, y):
    z = (1 + (x + y + 1)**2 * (19 - 14 * x + 3 * x**2 - 14 * y + 6 * x * y + 3 * y**2)) * \
        (30 + (2 * x - 3 * y)**2 * (18 - 32 * x + 12 * x**2 + 48 * y - 36 * x * y + 27 * y**2))
    return z

def rosenbrock(x, y):
    z = (1 - x)**2 + 100 * (y - x**2)**2
    return z

def f(x):
    z = x ** 4 - 2 * x ** 2
    return z

def gx2(x):
    z = 12 * x ** 2 - 4
    return z