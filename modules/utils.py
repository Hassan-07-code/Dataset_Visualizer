# modules/utils.py
import hashlib
import pandas as pd
import io

def fingerprint_df(df: pd.DataFrame) -> str:
    h = hashlib.sha256()
    h.update(pd.util.hash_pandas_object(df.head(10), index=True).values.tobytes())
    h.update(str(df.shape).encode())
    return h.hexdigest()[:12]

def to_bytes_io(s: str):
    bio = io.BytesIO()
    bio.write(s.encode("utf-8"))
    bio.seek(0)
    return bio
