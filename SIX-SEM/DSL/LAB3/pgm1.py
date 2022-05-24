n = int(input("Enter number: "))
print('1', end=' ')
for i in range(2,n):
 if n%i == 0:
  print(i, end=' ')
print(n)