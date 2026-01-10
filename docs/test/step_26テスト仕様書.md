# [Utilモジュール] 単体テスト仕様書

## 1. テスト目的
計算グラフ可視化モジュールである`Utilモジュール`を対象に、規定のディレクトリに正しく可視化したグラフを格納するか、正しいバイトサイズで生成しているかを確認する。

## 2. テスト対象クラス・メソッド

| 対象メソッド | 保存先 | 保存ファイル名 | 確認内容の要約 |
| --- | --- | --- |
| `plot_dot_graph` | `/app/docs/images/` | `test_graph.png` |  ファイルの存在確認とバイトサイズの確認 |

## 3. テストケース定義

### 3.1 正常系テスト (Normal Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 検証方法 |
| --- | --- | --- | --- | --- |
| N-01 | `test_graphviz` | `y(計算結果)`, `tmp_file = test_graph.png` | `os.path.exists(test_graph.png)` | `assertTrue` |
| N-02 | `test_graph_size` | `y(計算結果)`, `tmp_file = test_graph.png` | `os.path.getsize(test_graph.png, 0)` | `assertGreater` |

### 3.2 境界値・異常系テスト (Edge/Exception Cases)

| ID | テストケース名 | 入力値 (Input) | 期待される結果 (Expected) | 備考 |
| --- | --- | --- | --- | --- |
| E-01 | スカラー以外 | `y(計算結果)`, `tmp_file = test_graph.png` | 指定したファイルが存在しないこと |  |
| E-02 | 初期勾配なし | `y(計算結果)`, `tmp_file = test_graph.png` | `test_graph.png`の値が0より小さいこと |  |

## 4. 補足
- 今回のテストにおいては、画像ファイルを生成する必要がある
- テスト終了時(テストメソッドの終了地点)において、必ず生成した画像ファイルを削除すること
    * ``` if os.path.exists(tmp_file): os.remove(tmp_file)```