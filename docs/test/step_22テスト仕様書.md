# [Variableクラス追加機能] 単体テスト仕様書

## 1. テスト目的
スカラ値とVariableインスタンスで演算が行えるか確認

## 2. テスト対象クラス・メソッド

| 対象クラス | 対象メソッド | 確認内容の要約 |
| --- | --- | --- |
| `Variable` | `__sub__ `/ `__div__`/ `__neg__ `/ `__pow__` | インスタンス化を行わずスカラ値との演算が可能か確認 |
| `Variable` | `__rsub__ `/ `__rdiv__`| 右項と左項を入れ替えた場合で結果が正しく変わるか確認 |

## 3. テストケース定義

### 3.1 正常系テスト (Normal Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 検証方法 |
| --- | --- | --- | --- | --- |
| N-01 | test_sub | `x = Variable(np.array(5.0))`/`float 3.0` | `y.data == 2.0` | `assertEqual` |
| N-02 | test_rsub | `x = Variable(np.array(3.0))`/`float 5.0` | `y.data == -2.0` | `assertEqual` |
| N-03 | test_div | `x = Variable(np.array(6.0))`/`float 3.0` | `y.data == 2.0` | `assertEqual` |
| N-04 | test_rdiv | `x = Variable(np.array(3.0))`/`float 6.0` | `y.data == 2.0` | `assertEqual` |
| N-05 | test_pow | `x = Variable(np.array(2.0))`/`int 2` | `y.data == 4.0` | `assertEqual` |
| N-06 | test_neg | `x = Variable(np.array(3.0))` | `y.data == -3.0` | `assertEqual` |

### 3.2 境界値・異常系テスト (Edge/Exception Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 備考 |
| --- | --- | --- | --- | --- |
| E-01 | test_sub_error | `x0 = Variable(np.array(3.0))`と`a` を減算する | `TypeError` が返されること |  |
| E-02 | test_div_error | `x0 = Variable(np.array(3.0))`と`a` を除算する | `TypeError` が返されること |  |
| E-03 | test_pow_error | `x0 = Variable(np.array(3.0))`を`a` で累乗する | `TypeError` が返されること |  |
| E-04 | test_neg_error | `a` を負数にする | `TypeError` が返されること |  |

## 4. 数値微分による検証 (Gradient Check)

## 5. テストコード実装上の注意
