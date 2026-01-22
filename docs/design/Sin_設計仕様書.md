# [Sin] 設計仕様書

## 1. 概要
numpy.sinを使用した高階微分対応のSin関数

## 2. メソッド/関数 インターフェース

### `forward(self, x)`

* **引数**: `x` (ndarray)
* **計算** `y = np.sin(x)`
* **戻り値**: `y`

### `backward(self, gy)`

* **引数**: 出力側から伝播した勾配
* **計算**: `gx = gy * cos(self.inputs[0])`
* **戻り値**: `gx`

### ラッパー関数
* `sin = Sin()(x)`