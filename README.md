# nba-analytics-basketball-reference

# 🏀 NBA Analytics Suite — Basketball Reference Data (Python)

A fully featured NBA analytics project built using **Python, pandas, seaborn, and Basketball Reference data**.  
This project simulates a real-world data science workflow:

- data acquisition  
- cleaning & feature engineering  
- analytics  
- visualization  
- packaging into a modular codebase  

The goal is to showcase clean code, data engineering, and storytelling with data.

---

## 🚀 Features

### 🔗 Live Data Pull
Scrapes NBA per-game statistics from Basketball Reference using `pandas.read_html()`.

### 🧼 Data Cleaning
- Removes duplicate header rows  
- Converts numeric columns  
- Handles missing values  

### 🧮 Advanced Metrics Added
| Metric | Description |
|-------|-------------|
| **PTS_per36** | Scoring output normalized to 36 minutes |
| **Efficiency** | Custom metric combining offense, defense, and turnovers |

### 📈 Visualizations (Saved in `/visuals/`)
- Top scorers bar chart  
- Points vs assists scatterplot  
- Efficiency vs points  
- Scoring distribution by position  

---

## 📁 Project Structure

