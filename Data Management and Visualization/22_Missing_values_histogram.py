import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram():
    df = pd.read_csv("dataset.csv")

    plt.figure(figsize=(10,6))
    plt.hist(df["Salary"].dropna(), bins=10)
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.show()
