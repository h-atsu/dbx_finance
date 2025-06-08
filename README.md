# 株価予測 × ポートフォリオ最適化アプリケーション

## 概要

このプロジェクトは、過去の株価データをもとに機械学習で短期的なリターンを予測し、リスクを抑えた最適なポートフォリオを構築するアプリケーションです。

## 技術スタック

- 実行環境: Databricks クラスタ
- データ基盤: Delta Lake + dbt
- モデル管理: MLflow
- 開発環境: VSCode/Cursor

## セットアップ

1. リポジトリのクローン

```bash
git clone <repository-url>
cd stock_forecast_project
```

2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

3. 環境変数の設定
   `.env`ファイルを作成し、必要な環境変数を設定してください。

## 使用方法

```bash
python jobs/main.py --ticker AAPL --start-date 2023-01-01 --end-date 2023-12-31
```

## プロジェクト構造

```
stock_forecast_project/
├── src/          # ソースコード
├── jobs/         # ジョブ定義
├── notebooks/    # 分析用ノートブック
├── dbt/          # dbtモデル
└── requirements.txt
```

## ライセンス

MIT
