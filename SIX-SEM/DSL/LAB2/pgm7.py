print('OUTPUT : 7\n')

tuple1 =  (1,3,5,7,9,2,4,6,8,10)
c=0
n=len(tuple1)

for i in tuple1:
    c=c+1
    if c==int(n/2)+1:
        print()
    print(i,end=" ")
print("\n\n")