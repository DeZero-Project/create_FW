# [Utilモジュール] 設計仕様書

## 1. 概要
このモジュールはグラフの視覚化を行う補助機能の役割を持つ

## 2. メソッド/関数

### `get_dot_graph(output, verbose=True)`
- **役割**: 計算結果をdot形式に変換
- **引数**: `output`: 関数の結果。 `verbose`: Trueに変更した場合ndarrayインスタンスの形状とデータ型をdotに含める
- **戻り値**: `digraph g{\n txt}`: graphviz形式のテキスト。`txt`は`_dot_var`と`_dot_func`の出力結果をfor文でまとめたもの。
#### `add_func(f)`
- **役割**: 変数の世代を受取`set()`を用いて重複のないリストとして格納する補助メソッド
- **引数**: `f`: 変数の世代(`output.generation`)

### `_dot_var(v, verbose=False)`
- **役割**: `Variable`インスタンスの持つ属性をdot形式に変換する。
- **引数**: `v`: 変換するVariableインスタンス。 `verbose`: Trueに変更した場合Variableインスタンスの形状とデータ型をdotに含める
- **戻り値**: Variableインスタンスのidと属性をdot形式に変換したテキスト(`.format`を使用)

### `_dot_func(f)`
- **役割**: `Function`クラスが保管する入力値(`inputs`)、出力値(`outputs`)、変数の世代(`generation`)の関係性をdot形式に変換する
- **引数**: `f`: 変数の作成者(`creator`)
- **戻り値**: Functionインスタンスのidと属性の関係性をdot形式に変換したテキスト(`.format`を使用)

### `plot_dot_graph(output, verbose=True, to_file='graph.png')`
- **役割**: `get_dot_graph`の出力を画像に変換し保存。
- **引数**: `output`: 関数の結果, `verbose`:ndarrayインスタンスの形状とデータ型をdotに含めるフラグ, `to_file`: 画像保存時のファイル名
- **戻り値**: なし


## 3. 処理フロー

1. 関数の計算結果(`output`)を`get_dot_graph`で受け取る
2. `get_dot_graph`の`add_func`を利用し変数の世代をリスト化
3.  関数の結果の結果(`output`)を`_dot_var`に渡しVariableインスタンスをdot形式に整形
4. `add_func`でリスト化した関数を`pop()`を用いて１つずつ取り出し変数`txt`に足していく
5. `for`文を使い`add_func`のリストから関数の入力値(`funcs.inputs`)を取り出し`txt`に加算する
    * この際 `x.inputs` の`creator`がNoneではない場合`add_func`を使いリストに加える
6. `txt`の内容をdot形式に変更して返す(`digraph g {\n` + `txt` + `}`)