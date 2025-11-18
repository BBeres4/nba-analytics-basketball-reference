"""
clean_transform.py

Cleans the raw Basketball Reference table and adds advanced metrics.
"""

import pandas as pd

def clean_data(df):
    # Convert key stats to numeric values
    numeric_cols = ["PTS", "AST", "TRB", "STL", "BLK", "MP", "FG%", "3P%", "FT%"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Feature engineering
    df["PTS_per36"] = (df["PTS"] / df["MP"]) * 36
    df["Efficiency"] = (
        df["PTS"] + df["TRB"] + df["AST"] + df["STL"] + df["BLK"]
        - df["TOV"]
    )

    # Remove rows missing basic data
    df = df.dropna(subset=["PTS", "AST"])
    return df
