import mlflow
import argparse
import subprocess
import sys
from src.pipeline import run_pipeline

def main():
    # 依存関係のインストール
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="株価予測パイプライン")
    parser.add_argument("--ticker", type=str, required=True, help="対象の株式ティッカー")
    parser.add_argument("--start-date", type=str, help="開始日（YYYY-MM-DD形式）")
    parser.add_argument("--end-date", type=str, help="終了日（YYYY-MM-DD形式）")
    args = parser.parse_args()

    # MLflowの設定
    mlflow.set_tracking_uri("databricks")
    mlflow.set_experiment("/Users/yourname@domain.com/stock_forecast")

    # パイプラインの実行
    run_pipeline(
        ticker=args.ticker,
        start_date=args.start_date,
        end_date=args.end_date
    )

if __name__ == "__main__":
    main() 