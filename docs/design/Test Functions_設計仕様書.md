# [Test Functions] 設計仕様書

## 1. Factory Functions (sphere, matyas, goldstein_price, rosenbrock)

* **役割**: 最適化問題におけるテストを行う関数
* **引数**: `x`, `y`
* **戻り値**: `z`(全関数共通)
* **式**: 
    * **sphere**: `z = x**2 + y**2`

    * **matyas**: `z = 0.26(x**2 + y**2) - 0.48 * x * y`
    
    * **goldstein_price**: `z = (1 + x + y + 1)**2 * (19 - 14 * x + 3 * x**2 - 14 * y + 6 * x * y + 3 * y**2)\`
                            `(30 + (2 * x - 3 * y) * (18 - 32 * x + 12 * x**2 + 48 * y - 36 * x * y + 27 * y**2))`
    * **rosenbrock**: `z = (1 - x)**2 + 100 * (y - x**2)**2`