import sys
import pandas as pd

# Heart Disease Dataset
df = pd.read_csv('covid_19_data.csv')
df = df.dropna()
words1 = list(df['Country/Region'].values)
words2 = list(df['Confirmed'].values)

# Mapper output
for (word1, word2) in zip(words1, words2):
    print(f'{word1} \t {word2}')