# [Utilモジュール] 単体テスト仕様書

## 1. テスト目的
計算グラフ可視化モジュールである`Utilモジュール`を対象に、規定のディレクトリに正しく可視化したグラフを格納するか、正しいバイトサイズで生成しているかを確認する。

## 2. テスト対象クラス・メソッド

| 対象メソッド | 保存先 | 保存ファイル名 | 確認内容の要約 |
| --- | --- | --- |
| `plot_dot_graph` | `/app/docs/images/` | `test_graph.png` |  ファイルの存在確認とバイトサイズの確認 |

## 3. テストケース定義

### 3.1 正常系テスト (Normal Cases)

| ID | テストケース名 | 計算結果/保存先パス| 期待される結果 (Expected) | 検証方法 |
| --- | --- | --- | --- | --- |
| N-01 | `test_graphviz` | `y(計算結果)`/`tmp_file = /app/docs/images/test_graph.png` | `os.path.exists(tmp_file)` | `assertTrue` |
| N-02 | `test_graph_size` | `y(計算結果)`/`tmp_file = /app/docs/images/test_graph.png` | `os.path.getsize(tmp_file, 0)` | `assertGreater` |

### 3.2 境界値・異常系テスト (Edge/Exception Cases)

| ID | テストケース名 | 計算結果/保存先パス | 期待される結果 (Expected) | 備考 |
| --- | --- | --- | --- | --- |
| E-01 | `test_graphviz_error` | `y(計算結果)`/`tmp_file = /app/docs/images/test_graph.png` | `FileNotFoundError` |  |
| E-02 | `test_graph_size_error` | `y(計算結果)`/`tmp_file = /app/docs/images/test_graph.png` | `test_graph.png`の値が0より小さいこと |  |

## 4. 補足
- 今回のテストにおいては、画像ファイルを生成する必要がある
- テスト終了時(テストメソッドの終了地点)において、必ず生成した画像ファイルを削除すること
    * 正常系``` if os.path.exists(tmp_file): os.remove(tmp_file)```
    * 異常系``` os.remove(tmp_file)```