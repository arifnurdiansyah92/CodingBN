import pandas as pd

df = pd.read_json("./files/data.json")
print(df.head())