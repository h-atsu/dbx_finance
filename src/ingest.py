import subprocess
import sys

import yfinance as yf
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession


def install_requirements():
    """requirements.txtの依存関係をインストール"""
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
    )


def fetch_and_save_to_delta(ticker: str, start: str, end: str, delta_path: str):
    # 依存関係のインストール
    install_requirements()

    # データ取得
    df = yf.download(ticker, start=start, end=end)
    df.reset_index(inplace=True)

    # Sparkセッション作成
    builder = (
        SparkSession.builder.appName("StockIngest")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )
    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    # pandas → spark
    sdf = spark.createDataFrame(df)

    # Delta Lakeに保存
    sdf.write.format("delta").mode("overwrite").save(delta_path)
    print(f"Saved to {delta_path}")


if __name__ == "__main__":
    fetch_and_save_to_delta(
        "AAPL", "2023-01-01", "2023-12-31", "dbfs:/FileStore/bronze/stock_prices"
    )
