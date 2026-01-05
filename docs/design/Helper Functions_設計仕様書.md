# [Helper Functions] 設計仕様書

## 1. as_array

* **役割**: スカラー値を `ndarray` に変換し、NumPyの仕様による型エラーを回避する

## 2. numerical_diff

* **役割**: 中心差分近似を用いて数値微分を計算する
* **手順**:
1.  と  （）を計算
2. それぞれを関数 `f` に渡し、結果の差から微分値を求めて返す



## 3. Factory Functions (square, exp, add, mul, div, sub, neg)

* **役割**: 各演算クラス（Square, Exp, Add, Mul, Div, Sub, Pow. Neg）をインスタンス化して実行するラッパー関数


## 4. using_confif
* **役割**: Configで設定するフラグをwith構文で設定するため前処理と後処理を定義
* **引数**: `name`: 属性名  `value`: True/Falseを受け取る
* **処理**:  with構文での例外発生を想定しtry/finaryを使用
* **変数**: `old_value`:finalyブロック内で使用。with構文を抜ける際にフラグを元の値に戻す際に使用

## 5. no_grad
* **役割**: using_configを関数呼び出しだけで使用可能にする

## 6. as_variale
* **役割**: 引数に渡されたスカラー値をVariableインスタンスとして返す
* **処理**: 引数で受け取った値がVariableインスタンスだった場合はそのまま返す

## 7. rdiv
* **役割**: Divクラスに渡す値の前後を入れ替えDivクラスに渡す`x0, x1 -> x1, x0`
* **処理**: 渡された引数`x1`を`as_array` に渡して配列に変換した値をDivクラスに渡す

## 8. sub
* **役割**: Subクラスに渡す値の前後を入れ替えSubクラスに渡す`x0, x1 -> x1, x0`
* **処理**: 渡された引数`x1`を`as_array` に渡して配列に変換した値をSubクラスに渡す

## 9. pow
* **役割**: Variableインスタンスを定数(int)で累乗する
* **処理1**: 引数にVariableインスタンス`x` と定数`c`を受け取る
* **処理2**: `c`をinitに渡し`x`をforwardに渡して返す(`Pow(c)(x)`)
* **補足**: 累乗における右項はVariableインスタンス、左項が定数(int)として固定される仕様である