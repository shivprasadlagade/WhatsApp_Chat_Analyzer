import pandas as pd
from io import StringIO

def preprocessor(data):
    # If 'data' is a string containing CSV-formatted chat lines
    return pd.read_csv(StringIO(data))
