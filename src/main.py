"""
visualize.py

Creates polished, modern charts using seaborn and matplotlib.
"""

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid", font_scale=1.1)

def plot_top_scorers(df):
    top = df.sort_values("PTS", ascending=False).head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(data=top, x="PTS", y="Player", palette="Reds_r")
    plt.title("Top 10 NBA Scorers (2024)")
    plt.tight_layout()
    plt.savefig("visuals/top_scorers_bar.png")

def plot_pts_vs_ast(df):
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x="PTS", y="AST", hue="Pos", size="MP",
                    palette="coolwarm", alpha=0.7)
    plt.title("Points vs Assists — Colored by Position")
    plt.tight_layout()
    plt.savefig("visuals/pts_vs_ast.png")

def plot_efficiency(df):
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x="PTS", y="Efficiency", hue="Pos",
                    palette="viridis", alpha=0.7)
    plt.title("Player Efficiency vs Points")
    plt.tight_layout()
    plt.savefig("visuals/efficiency_scatter.png")

def plot_position_boxplot(df):
    plt.figure(figsize=(8,6))
    sns.boxplot(data=df, x="Pos", y="PTS")
    plt.title("Scoring Distribution by Position")
    plt.tight_layout()
    plt.savefig("visuals/position_boxplot.png")
