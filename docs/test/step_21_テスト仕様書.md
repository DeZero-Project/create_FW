# [Variableクラス追加機能] 単体テスト仕様書

## 1. テスト目的
スカラ値とVariableインスタンスで演算が行えるか確認

## 2. テスト対象クラス・メソッド

| 対象クラス | 対象メソッド | 確認内容の要約 |
| --- | --- | --- |
| `Variable` | `__rmul__ `/ `__radd__ ` / `__array_prority__` | 演算時において最優先で呼び出され演算されるか確認 |
| `Function` | `__call__` | 入力値が正しくVariableインスタンスとなっているか確認 |

## 3. テストケース定義

### 3.1 正常系テスト (Normal Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 検証方法 |
| --- | --- | --- | --- | --- |
| N-01 | test_radd | `x = Variable(np.array(2.0))`/`float 3.0` | `y.data == 5.0` | `assertEqual` |
| N-02 | test_radd | `x = Variable(np.array(3.0))`/`float 3.0` | `y.data == 9.0` | `assertEqual` |

### 3.2 境界値・異常系テスト (Edge/Exception Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 備考 |
| --- | --- | --- | --- | --- |
| E-01 | test_radd_error | `x0 = Variable(np.array(3.0))`と`a` を加算する | `TypeError` が返されること |  |
| E-02 | test_rmul_error | `x0 = Variable(np.array(3.0))`と`a` を乗算する | `TypeError` が返されること |  |

## 4. 数値微分による検証 (Gradient Check)

## 5. テストコード実装上の注意
* 修正に伴い`test_add_error`と`test_mul_error`のテストケースで期待される結果がTypeErrorに変わっている。
    * そのため今回、これらのテストケースも改修しテストを実施する