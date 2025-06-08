import mlflow
from typing import Optional

def run_pipeline(ticker: str, start_date: Optional[str] = None, end_date: Optional[str] = None):
    """
    株価予測パイプラインのメイン関数
    
    Args:
        ticker (str): 対象の株式ティッカー
        start_date (Optional[str]): 開始日（YYYY-MM-DD形式）
        end_date (Optional[str]): 終了日（YYYY-MM-DD形式）
    """
    with mlflow.start_run():
        mlflow.log_param("ticker", ticker)
        if start_date:
            mlflow.log_param("start_date", start_date)
        if end_date:
            mlflow.log_param("end_date", end_date)
            
        # TODO: データ取得、特徴量エンジニアリング、モデル学習、ポートフォリオ最適化の実装
        pass 