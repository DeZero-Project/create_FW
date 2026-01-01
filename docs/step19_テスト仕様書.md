# Variable クラス機能追加 単体テスト仕様書

## 1. テスト目的

`Variable` クラスに新しく追加された、データ属性（`shape`, `dtype`, `size`, `ndim`）へのアクセス機能、<br>
インスタンスへの名称付与（`name`）、および標準的な組み込み関数（`len`, `repr`）への対応が、意図通りに動作することを検証する。

## 2. テスト対象クラス・メソッド

| 対象クラス | 対象メソッド | 確認内容の要約 |
| --- | --- | --- |
| `Variable` | `shape`, `dtype`, `size`, `ndim` | 保持している `self.data` の各属性を正しく返却するか |
| `Variable` | `__init__` (name引数) | 引数で渡した名称が `self.name` に正しく保持されるか |
| `Variable` | `__len__` | データの第0次元の長さを正しく返すか |
| `Variable` | `__repr__` | インスタンスを print した際などに適切な文字列を返すか |

## 3. テストケース定義

### 3.1 正常系テスト (Normal Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 検証方法 |
| --- | --- | --- | --- | --- |
| **N-01** | データ属性の取得 | `data = np.array([[1, 2], [3, 4]])``v = Variable(data)` | `v.shape == (2, 2)``v.ndim == 2``v.size == 4``v.dtype == data.dtype` | `assertEqual` |
| **N-02** | 名称（エイリアス）の保持 | `v = Variable(np.array(1.0), name="input_x")` | `v.name == "input_x"` | `assertEqual` |
| **N-03** | デフォルト名の確認 | `v = Variable(np.array(1.0))` | `v.name is None` | `assertIsNone` |
| **N-04** | データ長の取得 (`__len__`) | `v = Variable(np.zeros((10, 2)))` | `len(v) == 10` | `assertEqual` |
| **N-05** | 文字列表現 (`__repr__`) | `v = Variable(np.array([1, 2]))` | `variable([1 2])` のような形式の文字列 | `assertEqual` |

---
### 3.2 境界値・異常系テスト (Edge/Exception Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 備考 |
| --- | --- | --- | --- | --- |
| E-01 | スカラーデータの `len` | `v = Variable(np.array(1.0))` | `TypeError` が発生する（numpyの仕様に準ずる場合） | スカラーに `len()` は適用不可 |
| E-02 | 空の名称付与 | `v = Variable(data, name="")` | `v.name == ""` | 空文字も許容されることを確認 |

## 4. 検証のポイント（エイリアス・インスタンス変数の確認）

設計書にある「エイリアスや値が正しく格納されているか」を確認するための具体的な考え方は以下の通りです。

* **エイリアス (`name`)**:
* コンストラクタで渡した文字列が、そのまま `v.name` というプロパティ（またはインスタンス変数）に格納されているかを、単純な比較 (`==`) で確認します。


* **データ属性 (`shape` など)**:
* `Variable` がラップしている `self.data` (NumPy配列) 自体が持つ属性と、`Variable` インスタンスから呼び出した値が一致するかを確認します。
* 例: `v.shape` を呼び出したときに、内部で `v.data.shape` を呼んでいるかをチェックする形になります。



## 5. テストコード実装上の注意

* **NumPyとの整合性**: `shape` や `dtype` の戻り値は NumPy の仕様に依存するため、比較対象も NumPy の属性を使用してください。
* **Propertyの確認**: 設計書に `@property` を使用するとあるため、テストコード上では `v.shape()` ではなく `v.shape` （括弧なし）でアクセスできることを確認する必要があります。

