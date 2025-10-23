import pandas as pd

def load_data(path="data/dechets-declares-a-fin-2023.csv"):
    df = pd.read_csv(path, sep=";", encoding="utf-8")
    return df
