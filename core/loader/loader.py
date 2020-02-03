import pandas as pd


def load_file():
    try:
        return pd.read_csv("./core/loader/data.csv")
    except FileNotFoundError as e:
        print(e)
