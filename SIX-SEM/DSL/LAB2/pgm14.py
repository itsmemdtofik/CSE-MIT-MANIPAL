import pandas as pd
print("OUTPUT : 14 \n")
dict={"Name":["Ram","Shyam","Mohan"],"Height":[150,120,170],"Qualification":["UG","PG","PhD"]}
df=pd.DataFrame(dict)
print(df)
print("\nAppending column using insert()")
gpa=[10,9,8]
df.insert(3, "GPA", gpa, allow_duplicates = False)
print(df)
print("\n")