# [DeZero自作学習プロジェクト]

> **[作りながら理解するFW学習]**

## 📌 概要 / Description。

* **目的**: [FW作成方法の学習]
* **主な特徴**:
* [特徴1：書籍を要件定義と考え設計を行ってから実装を行っている]
* [特徴2：コピペはせず自身で考えながら進めている]
* [特徴3：可搬性向上のためDockerを使用し環境構築を行う]



### 💡 設計ポリシー / Principles

* **Quality First**: 全てのコア機能に対してユニットテストを網羅し、安定性を担保する。
* **Keep It Simple**: 複雑な構成を避け、可読性とメンテナンス性を最優先する。

## 📚 出典・リファレンス / Credits & References

本プロジェクトの学習および開発にあたり、以下の著作物を参考にしています。

* **書籍**: [『ゼロから作るDeep Learning ❸ ―フレームワーク編』](https://www.oreilly.co.jp/books/9784873119069/)（斎藤 康毅 著、オライリー・ジャパン刊）
* **公式リポジトリ**: [oreilly-japan/deep-learning-from-scratch-3](https://github.com/oreilly-japan/deep-learning-from-scratch-3)

### 💡 学習ポリシー / Principles

* **Requirements-Driven Development**: 書籍の理論を「仕様」として抽出し、独自のUMLや設計図（`/docs`参照）を作成してから実装に入る。
* **No Copy-Paste**: 既存コードのコピー＆ペーストを禁止し、ロジックを自分なりに咀嚼してコードに落とし込む。
* **Quality First**: 全てのコア機能に対してユニットテストを網羅し、安定性を担保する。

---

## ⚖️ ライセンス / License

* 本リポジトリのコードおよびドキュメントは [MIT License](https://www.google.com/search?q=./LICENSE) に基づき公開されています。
* 参考にしている『ゼロから作るDeep Learning ❸』の公式コードは MIT License で公開されており、本プロジェクトはそのライセンスを尊重し作成されています。
* Copyright (c) 2024 kazu / Original Code Copyright (c) 2020 斎藤 康毅

---

## 🛠 技術スタック / Tech Stack

プロジェクトで使用している主要な技術群です。

| カテゴリ | 技術名 | 役割 / 採用理由 |
| --- | --- | --- |
| **Language** | [Python 3.10+] | [書籍準拠] |
| **Framework/Lib** | [numpy/cupy] | [テンソルに関する計算処理] |
| **Infrastructure** | [Docker] | [環境依存を排除したポータビリティの向上] |
| **Tooling** | [unittest] | [追加ライブラリを極力使わない実装方針でのテスト] |

---
## 🏗 アーキテクチャと設計方針 / Architecture

### 基本構成

* **[core_sinple.py](https://github.com/1206-1204-777/create_FW/blob/stage2/dezero/core_simple.py)**: [cupy未対応のコアロジック]
* **[variable_test.py](https://github.com/1206-1204-777/create_FW/blob/stage2/tests/variable_test.py)**: [core_simple内のVariableクラスに関するロジックテスト]
* **[util.py](https://github.com/1206-1204-777/create_FW/blob/stage3/dezero/util.py)**: [DeZeroで生成した計算グラフの可視化を行う補助モジュール]

### プロセスフロー

> **Note**: 設計の詳細は [/docs](https://github.com/1206-1204-777/create_FW/tree/stage2/docs) フォルダ内の設計書を参照してください。

---

## 📂 リポジトリ構成 / Repository Structure

```text
├──dezero/
│   ├── core/           # 基盤ロジック
├── docs/               # 設計ドキュメント・仕様書
├── example/            # 動作確認用スクリプト
├── tests/              # テストコード
├── Dockerfile          # 環境構築用Dockerfile
├── LICENSE             # 本リポジトリのライセンス
├── README.md           # 本ファイル
├── rule.yml            # 実装ルール
└── run.sh              # 起動用スクリプト
```
