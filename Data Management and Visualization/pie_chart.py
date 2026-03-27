import pandas as pd
import matplotlib.pyplot as plt

def plot_pie():
    df = pd.read_csv("dataset.csv")

    plt.figure(figsize=(8,8))
    df["Projects"].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Project Distribution")
    plt.ylabel("")
    plt.show()