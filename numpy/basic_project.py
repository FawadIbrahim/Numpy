import pandas as pd
import numpy as np


df=pd.read_csv('data.csv')
print(df.head())

print('Missing Values in each Column')
print(df.isnull().sum())

df['Calories'].fillna(df['Calories'].mean(),inplace=True)
df['Maxpulse'].fillna(df['Maxpulse'].median(),inplace=True)

df.replace([np.inf, -np.inf], np.nan,inplace=True)
df.fillna(df.mean(), inplace=True)

df.drop_duplicates(inplace=True)