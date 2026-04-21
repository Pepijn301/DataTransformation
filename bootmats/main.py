import pandas as pd

dataset = pd.read_csv('prices.csv')
dataset_cleaner = dataset.dropna()