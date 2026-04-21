import pandas as pd

df = pd.read_csv('prices.csv', sep="^")

print(df.info)