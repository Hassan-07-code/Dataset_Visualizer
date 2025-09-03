# modules/visualization.py
from typing import Tuple, Optional
import pandas as pd
import plotly.express as px
import numpy as np
from plotly.graph_objs import Figure

def generate_chart(
    df: pd.DataFrame,
    chart_type: str,
    x: Optional[str] = None,
    y: Optional[str] = None,
    title: Optional[str] = None
) -> Tuple[Figure, Optional[bytes]]:
    """
    Unified chart generator.
    Returns:
        fig (plotly.graph_objs.Figure): Interactive Plotly figure
        png_bytes (bytes|None): PNG image bytes (for PDF export fallback)
    """
    if df is None or df.empty:
        raise ValueError("Empty dataframe")

    chart_type = (chart_type or "line").lower()
    title = title or chart_type.title()

    # ---- Chart Selection ----
    if chart_type == "histogram":
        if x is None:
            raise ValueError("Histogram requires a column name for x")
        fig = px.histogram(df, x=x, nbins=30, title=title)

    elif chart_type == "bar":
        if x is None:
            raise ValueError("Bar chart requires x")
        if y is None:
            counts = df[x].value_counts(dropna=False).reset_index()
            counts.columns = [x, "count"]
            fig = px.bar(counts, x=x, y="count", title=title)
        else:
            fig = px.bar(df, x=x, y=y, title=title)

    elif chart_type == "scatter":
        if x is None or y is None:
            raise ValueError("Scatter requires x and y")
        fig = px.scatter(df, x=x, y=y, title=title)

    elif chart_type == "line":
        if x is None or y is None:
            raise ValueError("Line requires x and y")
        fig = px.line(df, x=x, y=y, title=title)

    elif chart_type == "pie":
        if x is None:
            raise ValueError("Pie requires a column name for values or names (x)")
        counts = df[x].value_counts(dropna=False).reset_index()
        counts.columns = [x, "count"]
        fig = px.pie(counts, names=x, values="count", title=title)

    elif chart_type == "box":
        if x is None:
            raise ValueError("Box requires a column name")
        fig = px.box(df, y=x, title=title)

    elif chart_type == "heatmap":
        nums = df.select_dtypes(include=[np.number])
        if nums.shape[1] == 0:
            raise ValueError("No numeric columns for heatmap")
        corr = nums.corr()
        fig = px.imshow(corr, text_auto=True, title=title)

    else:
        raise ValueError(f"Unknown chart type: {chart_type}")

    # ---- Styling ----
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        template="plotly_white"
    )

    # ---- PNG Export (optional) ----
    png_bytes = None
    try:
        png_bytes = fig.to_image(format="png")
    except Exception:
        # Skip silently if Kaleido not installed
        pass

    return fig, png_bytes
