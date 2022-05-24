import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plot
print("I/O Operations with external file : \n")
df = pd.read_csv('xyz.csv', header = None)
print(df.head())
print(df.tail())
df.columns = ['preg', 'glu', 'bp', 'sft', 'ins', 'bmi', 'dpf', 'age', 'class']
plot.scatter(df['bmi'], df['glu'])
plot.xlabel('bmi')
plot.ylabel('Glucose')
plot.show()
df['age'].hist()
plot.show()
f.plot(kind ='bar')
plot.show()
