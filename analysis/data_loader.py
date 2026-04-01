import pandas as pd
from pathlib import Path

def load_data():
    df = pd.read_csv(Path("data/processed/epl_master.csv"))

    df["TotalCards"] = df["HY"] + df["AY"]
    df["TotalFouls"] = df["HF"] + df["AF"]

    df["VAR_Era"] = df["Season"].apply(
        lambda x: "Post-VAR" if int(x[:4]) >= 2019 else "Pre-VAR"
    )

    return df
