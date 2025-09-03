import pandas as pd
from modules.data_summary import generate_data_summary

def test_generate_data_summary():
    df = pd.DataFrame({"A":[1,2,None],"B":["a","b","c"]})
    s = generate_data_summary(df)
    assert 'columns' in s and 'missing_values' in s and 'data_types' in s
    assert s['missing_values']['A'] == 1
