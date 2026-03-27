import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def check_missing():
    df = pd.read_csv("dataset.csv")

    print("Missing Values:\n", df.isnull().sum())

    plt.figure(figsize=(10,5))
    sns.heatmap(df.isnull(), cbar=False)
    plt.title("Missing Values Heatmap")
    plt.show()