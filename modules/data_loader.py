# modules/data_loader.py
import io
from typing import Tuple
import pandas as pd
from config.settings import MAX_UPLOAD_SIZE_MB


ALLOWED_EXT = {".csv", ".xls", ".xlsx"}


def _get_size_bytes(uploaded_file) -> int:
    try:
        uploaded_file.seek(0, io.SEEK_END)
        size = uploaded_file.tell()
        uploaded_file.seek(0)
        return size
    except Exception:
        # fallback - no size
        return 0


def validate_upload(uploaded_file) -> None:
    """Raise ValueError if not valid."""
    if uploaded_file is None:
        raise ValueError("No file provided.")
    name = getattr(uploaded_file, "name", "")
    if not any(name.lower().endswith(ext) for ext in ALLOWED_EXT):
        raise ValueError("Unsupported file type. Allowed: .csv, .xls, .xlsx")
    size = _get_size_bytes(uploaded_file)
    if size and size > MAX_UPLOAD_SIZE_MB * 1024 * 1024:
        raise ValueError(f"File too large ({round(size/1024/1024,2)} MB). Max allowed is {MAX_UPLOAD_SIZE_MB} MB.")


def load_data(uploaded_file) -> Tuple[pd.DataFrame, dict]:
    """
    Read a Streamlit UploadedFile-like object and return (df, meta).
    meta contains filename, size_bytes, rows, cols.
    """
    validate_upload(uploaded_file)
    name = uploaded_file.name
    uploaded_file.seek(0)
    if name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        # xls / xlsx
        df = pd.read_excel(uploaded_file, engine="openpyxl")
    meta = {"filename": name, "size_bytes": _get_size_bytes(uploaded_file), "rows": df.shape[0], "cols": df.shape[1]}
    return df, meta


def sample_preview(df, n=10):
    return df.head(n).copy()
