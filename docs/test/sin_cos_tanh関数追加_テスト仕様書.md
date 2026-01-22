# [sin/cos/tanh関数追加] 単体テスト仕様書

## 1. テスト目的
高階微分に対応したsin/cos/tanh関数追加に伴うテスト

## 2. テスト対象クラス・メソッド

| 対象クラス | 対象メソッド | 確認内容の要約 |
| --- | --- | --- |
| `Sin` | `backward` | 逆伝播において正しく演算が行えているかの確認 |
| `Cos` | `backward` | 逆伝播において正しく演算が行えているかの確認 |
| `Tanh` | `backward` | 逆伝播において正しく演算が行えているかの確認 |


## 3. テストケース定義


### 3.1 正常系テスト (Normal Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 検証方法 |
| --- | --- | --- | --- | --- |
| N-01 | 計算結果の確認 | `x = Variable(np.array([2.0]))` | `np.allclose(y.grad, sin(x.data), atol=1e-8)`  | `assertTrue` |
| N-02 | 計算結果の確認 | `x = Variable(np.array([2.0]))` | `np.allclose(y.grad,numerical_diff(sin, x), atol=1e-8)`  | `assertTrue` |
| N-03 | 計算結果の確認 | `x = Variable(np.array([2.0]))` | `np.allclose(y.grad, tanh(x.data), atol=1e-8)`  | `assertTrue` |

### 3.2 異常系テスト (Exception Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 備考 |
| --- | --- | --- | --- | --- |
| E-01 | ndarray以外を渡した場合 | `sin('a')` | `TypeError` |  |
| E-02 | ndarray以外を渡した場合 | `cos('a')` | `TypeError` |  |
| E-03 | ndarray以外を渡した場合 | `tanh('a')` | `TypeError` |  |

### 4 注意事項
- 今回の関数はスカラを返す設計のため、そのままではVariabreクラスでエラーになる
    - 対策として、入力値を1次元配列にすることで計算後もndarrayとして渡すことが可能になる