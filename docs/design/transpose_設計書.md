# [transpose機能] 設計仕様書

## 1. 概要
- numpy.trasposeを用いてVariabeleインスタンスの転置を行う関数
## 2. クラス 定義

| 変数名 | 型  | 説明 | 備考 |
| --- | --- | --- | --- |
| `axes` | `int` | 転置を行う軸の指定 |  |
| `axes_len` | `int` | `axes`の値を格納する |  |
| `inv_axes` | `int` | 正規化を行なった軸指定をタプルに変換した値を格納 |  |
| `y` | `ndarray` | 転置を行なった後の値 | `forward`の戻り値として使用する |

## 3. Transpose(Function)
### `__init__(self, axes=None)`
* **役割**: 引数で渡された`axes`の指定をインスタンス変数に格納する

### `forward(self, x, axes=0)`

* **役割**: 引数で渡された`x`の行列を入れ替える
* **処理フロー**: `y = np.transpose(x)`でxの形状を転置し、`y`を返す

### `backward(self, gy)`

* **役割**: `transpose`関数を用いて、逆伝播における勾配を転置して返す
* **処理フロー1**:`self.axes`がNoneか確認する
    * **処理フロー2**:Noneだった場合は、`transpose`に`gy`をそのまま渡す
* **処理フロー3**: Noneでなかった場合は、`axes_len = len(self.axes)`で指定された軸の値を取り出す
* **処理フロー4**: `inv_axes = tuple(np.argsort([ax % axes_len for ax in self.axes]))` を用いて正規化した軸指定をタプルに変換
* **処理フロー5**:`transpose(gy, inv_axes)` を戻り値として返す
## 4. transpose
* **役割**: `transpose`クラスの逆伝播時において、逆伝播における勾配を転置して返すための補助関数
* **プロトタイプ**: `transpose(x, axes=None)`
* **処理フロー**: `Transpose(axes)(x)`を返す