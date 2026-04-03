import pandas as pd
import matplotlib.pyplot as plt

def plot_line():
    df = pd.read_csv("dataset.csv")

    plt.figure(figsize=(10,6))
    plt.plot(df["ID"], df["Score"], marker='o')
    plt.title("Score Trend")
    plt.xlabel("ID")
    plt.ylabel("Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
