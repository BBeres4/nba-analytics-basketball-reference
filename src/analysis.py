"""
analysis.py

Contains analysis functions for identifying top players and interesting patterns.
"""

def top_scorers(df, n=10):
    return df[["Player", "PTS"]].sort_values("PTS", ascending=False).head(n)

def underrated_players(df):
    """
    Finds efficient players who play relatively few minutes but produce at a high level.
    """
    return df[
        (df["Efficiency"] > df["Efficiency"].quantile(0.75)) &
        (df["MP"] < 25)
    ][["Player", "PTS", "MP", "Efficiency"]]
