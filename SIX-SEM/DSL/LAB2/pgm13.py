import pandas as pd
print("OUTPUT : 13\n")
dict={"Name":["Ram","Shyam","Mohan"],"Height":[150,120,170],"Qualification":["UG","PG","PhD"]}
df=pd.DataFrame(dict)
print(df)


address=["Delhi","Mumbai","Hyderabad"]
print("\nAppending address:- ")
df['Address']=address
print(df)
print("\n\n")