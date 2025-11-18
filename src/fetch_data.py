"""
fetch_data.py

Loads NBA per-game statistics from Basketball Reference using pandas.read_html().
"""

import pandas as pd

def load_bbr_data():
    """
    Fetches the NBA per-game stats table for the 2024 season.
    Returns a cleaned pandas DataFrame (duplicate headers removed).
    """
    url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
    tables = pd.read_html(url)
    df = tables[0]

    # Remove repeated header rows inside the table
    df = df[df['Player'] != "Player"]
    return df


if __name__ == "__main__":
    print(load_bbr_data().head())
