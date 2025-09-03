import pandas as pd
from typing import Dict, Any

def generate_data_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Returns a dict with keys: columns, data_types, missing_values, shape, sample (list of rows)
    Designed to match your tests that check for 'columns', 'missing_values', 'data_types'
    """
    if df is None:
        return {"error": "No data provided"}
    if df.empty:
        return {"error": "Empty dataset"}

    summary = {}
    summary["shape"] = {"rows": int(df.shape[0]), "columns": int(df.shape[1])}
    summary["columns"] = df.columns.tolist()
    summary["data_types"] = df.dtypes.astype(str).to_dict()
    summary["missing_values"] = df.isnull().sum().to_dict()
    summary["duplicate_rows"] = int(df.duplicated().sum())
    summary["sample"] = df.head(5).to_dict(orient="records")
    return summary
