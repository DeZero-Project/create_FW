# [Helper Functions] 設計仕様書

## 1. as_array

* **役割**: スカラー値を `ndarray` に変換し、NumPyの仕様による型エラーを回避する。

## 2. numerical_diff

* **役割**: 中心差分近似を用いて数値微分を計算する。
* **手順**:
1.  と  （）を計算。
2. それぞれを関数 `f` に渡し、結果の差から微分値を求めて返す。



## 3. Factory Functions (square, exp, add)

* **役割**: 各演算クラス（Square, Exp, Add）をインスタンス化して実行するラッパー関数。

## 4. using_confif
* **役割**: Configで設定するフラグをwith構文で設定するため前処理と後処理を定義。
* **引数**: `name`: 属性名  `value`: True/Falseを受け取る。
* **処理**:  with構文での例外発生を想定しtry/finaryを使用。
* **変数**: `old_value`:finalyブロック内で使用。with構文を抜ける際にフラグを元の値に戻す際に使用。

## 5. no_grad
* **役割**: using_configを関数呼び出しだけで使用可能にする
