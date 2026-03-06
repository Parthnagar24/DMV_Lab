import pandas as pd

data = {"Age": [20, None, 25, None, 30]}

df = pd.DataFrame(data)


print(df.isnull())