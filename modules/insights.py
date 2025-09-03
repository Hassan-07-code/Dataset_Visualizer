# modules/insights.py
import pandas as pd
import numpy as np
from typing import Dict, Any, List

def generate_insights(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Return: {'summary': DataFrame, 'correlation': DataFrame, 'bullets': [str,...]}
    """
    if df is None or df.empty:
        return {"error": "No data"}

    nums = df.select_dtypes(include=[np.number])
    summary = nums.describe().T if not nums.empty else pd.DataFrame()
    corr = nums.corr() if not nums.empty else pd.DataFrame()

    bullets: List[str] = []

    # missing value bullets
    missing = df.isnull().sum()
    high_missing = missing[missing > 0]
    for col, m in high_missing.items():
        pct = round(100 * m / max(1, len(df)), 2)
        bullets.append(f"Column **{col}** has {m} missing values ({pct}%).")

    # top correlations
    if not corr.empty:
        corr_unstacked = corr.where(~np.eye(corr.shape[0], dtype=bool)).stack().abs().sort_values(ascending=False)
        top_pairs = corr_unstacked.drop_duplicates().head(5)
        for (a, b), val in top_pairs.items():
            signed = corr.loc[a, b]
            bullets.append(f"**{a}** and **{b}** correlation = {signed:.2f}.")

    if not bullets:
        bullets.append("No major issues detected. Dataset looks ready for exploration.")

    return {"summary": summary, "correlation": corr, "bullets": bullets}
