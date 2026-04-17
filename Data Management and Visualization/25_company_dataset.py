import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("company_dataset.csv")


df.columns = df.columns.str.strip()

df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')


df['years'] = df['years'].astype(str).str.extract(r'(\d+)')
df['years'] = pd.to_numeric(df['years'], errors='coerce')


df['review_count'] = df['review_count'].astype(str)
df['review_count'] = df['review_count'].str.replace('[(),]', '', regex=True)
df['review_count'] = df['review_count'].str.replace(' Reviews', '', regex=False)
df['review_count'] = df['review_count'].str.replace('k', '', regex=False)
df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce') * 1000

# Employees conversion
def convert_employees(val):
    if pd.isna(val):
        return None
    val = str(val)

    if "1 Lakh" in val:
        return 100000
    elif "50k-1 Lakh" in val:
        return 75000
    elif "10k-50k" in val:
        return 30000
    elif "5k-10k" in val:
        return 7500
    elif "1k-5k" in val:
        return 3000
    else:
        return None

df['employees'] = df['employees'].apply(convert_employees)

df = df.dropna(subset=['employees'])


df_sample = df.copy()


#pie chart
top10 = df_sample.nlargest(10, 'employees')
plt.figure(figsize=(8, 8))
plt.pie(top10['employees'], labels=top10['name'], autopct='%1.1f%%')
plt.title("Top 10 Companies by Employees")
plt.show()


#funnel chart
rating_group = df_sample['ratings'].value_counts().sort_values(ascending=True)
plt.figure(figsize=(8, 5))
plt.barh(rating_group.index.astype(str), rating_group.values, color='purple')
plt.title("Funnel Chart (Ratings Distribution)")
plt.xlabel("Count")
plt.ylabel("Ratings")
plt.show()

#bar chart
top_years = df_sample.nlargest(15, 'years')
plt.figure(figsize=(10, 6))
sns.barplot(data=top_years, x='years', y='name', palette='coolwarm')
plt.title("Top Companies by Years")
plt.show()

#line chart
ctype_count = df_sample['ctype'].value_counts()
plt.figure(figsize=(8, 5))
plt.plot(ctype_count.index, ctype_count.values, marker='o')
plt.title("Company Type Distribution (Line Chart)")
plt.xlabel("Company Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

#Histogram
plt.figure(figsize=(8, 5))
sns.histplot(df_sample['review_count'], bins=20, kde=True, color='green')
plt.title("Review Count Distribution")
plt.xlabel("Review Count")
plt.show()