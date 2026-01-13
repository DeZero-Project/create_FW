# [最適化問題テスト用関数] 単体テスト仕様書

## 1. テスト目的
最適化問題に関する関数の単体テスト

## 2. テスト対象クラス・メソッド

| 対象クラス | 対象メソッド | 確認内容の要約 |
| --- | --- | --- |
| --- | `sphere` | 計算結果後の逆伝播が正しいかを確認 |
| --- | `matyas` | 計算結果後の逆伝播が正しいかを確認 |
| --- | `goldstein_price` | 計算結果後の逆伝播が正しいかを確認 |

## 3. テストケース定義

### 3.1 正常系テスト (Normal Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 検証方法 |
| --- | --- | --- | --- | --- |
| N-01 | `test_sphere` | `x0 = Variable(np.array(1.0))`, `x1 = Variable(np.array(1.0))` | `x0.grad == 2.0`. `x1.grad == 2.0` | `assertEqual` |
| N-02 | `test_matyas` | `x0 = Variable(np.array(1.0))`, `x1 = Variable(np.array(1.0))` | `x0.grad == 040000000000000036`. `x1.grad == 040000000000000036` | `assertEqual` |
| N-03 | `test_goldstein_price` | `x0 = Variable(np.array(1.0))`, `x1 = Variable(np.array(1.0))` | `x0.grad == -5376.0 `. `x1.grad == 8064.0` | `assertEqual` |
### 3.2 境界値・異常系テスト (Edge/Exception Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 備考 |
| --- | --- | --- | --- | --- |
| E-01 | `test_sphere_error` | `x0 = Variable(np.array(1.0))`,`a` | `TypeError` |  |
| E-02 | `test_matyas_error` | `x0 = Variable(np.array(1.0))`,`a` | `TypeError` |  |
| E-03 | `test_goldstein_price_error` | `x0 = Variable(np.array(1.0))`,`a` | `TypeError` |  |

## 4. 数値微分による検証 (Gradient Check)

## 5. テストコード実装上の注意
