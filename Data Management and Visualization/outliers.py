import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def detect_outliers():
    df = pd.read_csv("dataset.csv")

    plt.figure(figsize=(8,6))
    sns.boxplot(y=df["Salary"])
    plt.title("Salary Outliers")
    plt.show()