import io
from modules.data_loader import load_data

def test_load_csv_bytesio():
    csv = "a,b,c\n1,2,3\n4,5,6\n"
    f = io.BytesIO(csv.encode("utf-8"))
    f.name = "test.csv"
    df, meta = load_data(f)
    assert df.shape == (2, 3)
    assert meta["filename"] == "test.csv"
