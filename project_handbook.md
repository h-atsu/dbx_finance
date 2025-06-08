
# 📘 プロジェクト引き継ぎメモ for Cursor

## 🧭 プロジェクト名
株価予測 × ポートフォリオ最適化アプリケーション（Databricksクラスタ上で実行、VSCode/Cursorでローカル編集）

---

## 1. 🎯 プロジェクト目的と概要

- 過去の株価データをもとにMLで短期的なリターンを予測し、リスクを抑えた最適なポートフォリオを構築する
- データの保存・分析にはDatabricksを利用し、クラスタ上で実行
- ローカル（VSCode or Cursor）から `.py` スクリプトを編集・バージョン管理
- データ基盤は Delta Lake + dbt による三層管理（bronze/silver/gold）

---

## 2. 🧱 技術スタックと開発方針

| 項目 | 内容 |
|------|------|
| エディタ | VSCode または Cursor |
| 実行環境 | Databricks クラスタ |
| スクリプト構成 | `.py` ファイル中心、NotebookはEDA/可視化に限定 |
| パッケージ管理 | `poetry`は使用せず、`subprocess + pip install -r requirements.txt` 方式 |
| モデル管理 | MLflow（tracking URI = Databricks） |
| DWH管理 | dbt-core + Databricks adapter |
| CI/CD連携（将来） | Git + Databricks Job API or CLI（オプション） |

---

## 3. 📂 ディレクトリ構成（ローカル開発）

```
stock_forecast_project/
├── src/
│   ├── ingest.py
│   ├── features.py
│   ├── model.py
│   ├── optimize.py
│   └── pipeline.py
├── jobs/
│   └── main.py
├── notebooks/
│   └── 01_eda.ipynb
├── dbt/
│   ├── models/
│   ├── dbt_project.yml
│   └── profiles.yml
├── requirements.txt
├── .env
├── README.md
```

---

## 4. 🔁 ローカル ↔ Databricks の連携方針

- 実行対象は Databricks のクラスタ
- ローカルから編集した `.py` を Job としてクラスタ上で実行
- `requirements.txt` を `subprocess` 経由で実行し依存解決
- `dbfs:/FileStore/requirements.txt` に事前アップロードしておくのが望ましい
- MLflowログは `mlflow.set_tracking_uri("databricks")` を指定してDatabricksに記録

---

## 5. 🛠️ 開発フローの一例

1. VSCode/Cursorで `.py` ファイルを編集
2. デバッグ時はローカル環境で実行（仮想環境で依存解決）
3. `jobs/main.py` にて `argparse` でパラメータ渡し可能なCLIインタフェースを提供
4. Databricks Job UI または APIで `.py` をクラスタ上で実行
5. 結果は Delta Tableに保存 + MLflowに記録
6. dbtを使ってマート化し、Databricks SQLで可視化またはダッシュボードに反映

---

## 6. ✅ MLflowとJob連携例（コード）

```python
import mlflow
import argparse
import subprocess
import sys
from src.pipeline import run_pipeline

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

parser = argparse.ArgumentParser()
parser.add_argument("--ticker", type=str, required=True)
args = parser.parse_args()

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Users/yourname@domain.com/stock_forecast")

run_pipeline(ticker=args.ticker)
```

---

## 7. ⛳ 想定される今後の展開

- Databricks Job JSON構成ファイルを用意して、GitOps的にJob管理
- dbtモデルの拡充（セクター別パフォーマンス分析など）
- AirflowやGitHub ActionsによるCI/CD化
- DashやStreamlitによる外部ダッシュボードとの連携（任意）
