import pandas as pd

def clean_and_transform(data):
    df = pd.DataFrame(data)
    df["description"] = df["description"].str.strip()
    df["status"] = df["status"].fillna("Unknown")
    return df
