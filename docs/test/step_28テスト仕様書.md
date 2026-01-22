# [rosenbrock関数] 単体テスト仕様書

## 1. テスト目的
最適化問題に追加したrosenbrock関数の単体テスト

## 2. テスト対象クラス・メソッド

| 対象クラス | 対象メソッド | 確認内容の要約 |
| --- | --- | --- |
| --- | `rosenbrock` | 計算結果後の逆伝播が正しいかを確認 |


## 3. テストケース定義

### 3.1 正常系テスト (Normal Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 検証方法 |
| --- | --- | --- | --- | --- |
| N-01 | `test_rosenbrock_minimum` | `x0 = Variable(np.array(1.0))`, `x1 = Variable(np.array(1.0))` | `z.data == 0.0` ,`x0.grad == -0.0 ` ,`x1.grad == 0.0 ` | `assertEqual` |
| N-02 | `test_rosenbrock_origin`| `x0 = Variable(np.array(0.0))`, `x1 = Variable(np.array(0.0))` | `z.data == 1.0`, `x0.grad == -2.0 ` ,`x1.grad == 0.0 `  | `assertEqual` |

### 3.2 異常系テスト (Exception Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 備考 |
| --- | --- | --- | --- | --- |
| E-01 | `test_rosenbrock_error` | `x0 = Variable(np.array(1.0))`,`"a"` | `TypeError` |  |
| E-02 | `test_rosenbrock_none_error` | `x0 = Variable(np.array(1.0))`,`None` | `TypeError` |  |
