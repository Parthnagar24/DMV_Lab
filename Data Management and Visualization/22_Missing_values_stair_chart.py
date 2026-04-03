import pandas as pd
import matplotlib.pyplot as plt

def plot_stair():
    df = pd.read_csv("dataset.csv")

    plt.figure(figsize=(10,6))
    plt.step(df["ID"], df["Sales"], where='mid')
    plt.title("Sales Stair Chart")
    plt.xlabel("ID")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.show()
