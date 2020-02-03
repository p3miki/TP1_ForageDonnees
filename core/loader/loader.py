import pandas as pd


def load_file():
    try:
        return pd.read_csv("./core/loader/data.csv", index_col="Rank")
    except FileNotFoundError as err:
        print(err)
