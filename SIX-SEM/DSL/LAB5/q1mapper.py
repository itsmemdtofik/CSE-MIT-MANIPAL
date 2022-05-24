import sys
import pandas as pd
df = pd.read_csv("covid_19_data.csv")
l = df['Country/Region'].tolist()
for x in l:
    print("%s\t%s"%(x,1))