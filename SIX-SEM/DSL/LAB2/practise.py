import pandas as pd
import numpy as np

print("Creating a DataFrame Using Dictionary : \n")
s = pd.Series([3, 9, -2, 10, 5])
print(s.sum())
print(s.min())
print(s.max())

print("\n")
print("Creating a Data Frame : ")
data = [['Dinesh', 10], ['Nithya', 12], ['Raji', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

print("Indexed Data Frame : ")
data = {'Name': ['Kavitha', 'Sudha', 'Raju',
                 'Vignesh'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])

print(df.shape)
print(df.dtypes)
print(df.head())
print(df.tail())
df1 = pd.DataFrame({'A': pd.Timestamp('20130102'), 'B': np.array([3]*4, dtype='int32'),
                    'C': pd.Categorical(['Male', 'Female', 'Male', 'Female'])})

print(df1.shape)
print(df1.dtypes)
print(df1.head())
print(df1.tail())

print("\n")
dates = pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100, 4), index=dates, columns=list('ABCD'))

print(df.head())
print(df.tail())
print(df.index)
print(df.columns)
print("\n")
df.sort_index(axis=1, ascending=False)
print(df.head())
print("\n")
df.sort_values(by='B')
print(df.head())

print("\nslicing")
print(df['20130105':'20130110'])

print("\n")
print(df.iloc[0])
print("\n")
print(df.iloc[0, :2])
print("\n")
print(df['A'])
dates = pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100, 4), index=dates, columns=list('ABCD'))
df1 = pd.DataFrame({'A': pd.Timestamp('20130102'), 'B': np.array([3]*4, dtype='int32'),
                    'C': pd.Categorical(['Male', 'Female', 'Male', 'Female'])})
df2 = pd.DataFrame({'A': pd.Timestamp('20130102'), 'B': np.array([3]*4, dtype='int32'),
                    'C': pd.Categorical(['Male', 'Female', 'Male', 'Female'])})


print("\nboolean indexing : ")
print(df[df.A > 0])

print("\n")
df.loc[:, 'D'] = np.array([5]*len(df))

print("\ndeleting column : ")
df.drop('A', axis=1, inplace=True)

s=pd.Series([3,9,-2,10,5])
print(s.sum())
print(s.min())
print(s.max())


print("\n")
print("Creating a Data Frame : ")
data = [['Dinesh',10],['Nithya',12],['Raji',13]]
df = pd.DataFrame(data,columns=['Name','Age'])

print("Indexed Data Frame")
data = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])

print(df.shape)
print(df.dtypes)
print(df.head())
print(df.tail())


