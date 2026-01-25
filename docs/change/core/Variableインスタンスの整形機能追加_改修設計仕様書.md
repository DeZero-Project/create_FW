# [Variableインスタンスの整形機能追加] 改修設計仕様書

## 1. 改修の目的・背景
- **背景**: [Variableインスタンスの形状をそのまま整形できるよう修正することで、利便性が向上すると考えたため]
- **目的**: [Variableクラスにreshapeメソッドを追加して、Variableインスタンスの形状を直接整形できるようにする]

## 2. 変更内容一覧

| クラス名 | 関数/メソッド名 | 変更の概要 |
| :--- | :--- | :--- |
| `Variable` | `reshape` | 引数を整形し `function/reshape`へタプルとして渡すメソッドを追加 |
| `Variable` | `transpose` | Variableインスタンスを `function/transpose`へ渡すメソッドを追加|
| `Variable` | `T` | Variableインスタンスを `function/transpose`へ渡す際に使用するプロパティを追加|

## 3. 詳細設計（Before & After）

### 3.1 [reshape]
#### 変更前 (Before)
- [Variableインスタンスの形状を変えるには、`function/reshape`へタプルを直接渡す必要があった]

#### 変更後 (After)
* **プロトタイプ**: `reshape(self, *shape)`
* **処理フロー1**: `shape`の長さが1であり、`shape[0]`の形状が配列かタプルかを条件分岐で確認
    * **処理フロー2**: 条件が真だった場合は、`shape = shape[0]`とする
* **戻り値**: `dezero.function.reshape(self, shape)`

### 3.2 [transpose]
#### 変更前 (Before)
- [Variableインスタンスの転置を行えるのはndarrayのみであり、Variableインスタンスを直接転置することはできなかった]

#### 変更後 (After)
* **プロトタイプ**: `reshape(self, *axes)`
* **処理フロー1**: `axes`が0か確認する
    * **処理フロー2**: 条件が真だった場合は、axesをNoneにする
* **処理フロー3**: 条件が偽だった場合は`axes`の長さが1であることを確認する。    
    * **処理フロー2**: 条件分岐を用いて `axes[0]`の形状が配列かタプルか、またはNoneであるかを確認
        * **処理フロー3**: 条件が真だった場合は、`axes = axes[0]` で最初の要素を取り出す
* **戻り値**: `dezero.function.reshape(self, axes)`

### 3.2 [T]
#### 変更前 (Before)
- [Variableインスタンスの転置を行うには、transpseを毎回呼び出す必要があった]

#### 変更後 (After)
* **アノテーション**: `@property`
* **プロトタイプ**: `T(self)`
* **戻り値**: `dezero.function.transpose(self)`

## 4. 影響範囲と整合性
- **関連1**: `Variable`クラスに`reshape`メソッド、`transpose`メソッド、`T`メソッドを追加する必要がある

## 5. テスト・検証項目
- [X] 変更後Variableインスタンスの形状を直接変更できているか確認
