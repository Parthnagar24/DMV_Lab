import pandas as pd
import matplotlib.pyplot as plt

def plot_bar():
    df = pd.read_csv("dataset.csv")
    
    plt.figure(figsize=(10,6))
    df.groupby("Age")["Salary"].mean().plot(kind='bar', color='skyblue')
    plt.title("Average Salary by Age")
    plt.xlabel("Age")
    plt.ylabel("Average Salary")
    plt.tight_layout()
    plt.show()