# [Sumクラス] 設計仕様書

## 1. 概要
numpy.sumを利用し、軸指定と次元保持フラグを有した配列の圧縮を行う
## 2. クラス 定義


| 変数名 | 型 | 説明 | 備考 |
| :--- | :--- | :--- | :--- |
| `self.axis` | `スカラ型` | 呼び出し元が指定した次元数 | |
| `keepdims` | `論理型` | `True`の場合、元の次元数を保持し`False`なら次元数を減らす |  |

## 3. メソッド/関数 

### `__init__(self, axis, keepdims)`
- **役割**: `axis`と`keepdims`をインスタンス変数に格納

#### 処理フロー
- `self.axis = axis`
- `self.keepdims = keepdims`

### `forward(self, x)`
- **役割**: `x`の形状をインスタンス変数格納
- **役割**: numpy.sumを利用し指定した次元数へ値をまとめる
- **引数`x`**: 呼び出し元で渡されたnumpy配列
- **戻り値**: `y`

#### 処理フロー

**変数名一覧**
| 変数名 | 説明 | 使用箇所 | 補足 |
| :--- | :--- | :--- | :--- |
| `self.x_shape` | 引数`x`の形状を補完 | bakward処理時 |  | 

1. **初期化**: `self.x_shape = x.shape`で`x`の形状を補完
2. **演算処理**: `x.sum(axis = self.axis, keepdims = elf.keepdims)`の結果を`y`に格納

### `backward(self, gy)`
- **役割**: `broadcast_to`を用いて勾配を入力時の形状に直して返す
- **引数`gy`**: 逆伝播で受け取った勾配
- **戻り値**: `gx`

#### 処理フロー

**変数名一覧**
| 変数名 | 説明 | 使用箇所 | 補足 |
| :--- | :--- | :--- | :--- |
| `gy` | `utils_reshape_sum_backward`を用いて、入力時の形状にリシェイプした値を格納 | 処理開始直後 |  | 

1. **リシェイプ処理**: `utils_reshape_sum_backward(gy, axis = self.axis, keepdims = elf.keepdims)`で`gy`の値をリシェイプし`gy`に格納する
2. **ブロードキャスト処理**: `broadcast_to(gy, self.x_shape)`を使用し勾配の形状を`x_shape`と同じ形状に直す