import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plot

df = pd.read_table("myTxtFile.txt")
print(df.head())
f = df["Department"].value_counts()
print(f)
f.plot(kind = 'bar')
plot.show()
f.plot(kind = 'pie')
plot.show()
foo = pd.crosstab(df['Gender'], df['Attrition'])
foo.plot(kind ='bar')
plot.show();
