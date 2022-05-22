from typing import Counter

counter = 100
miles = 1000
name = "Mohammad Tofik"
print(counter)
print(miles)
print(name)
if counter > 10:
	print("This is good Idea !\n")
elif(counter != 100):
	print("It is More dangerous challenge thing\n")
else:
	print("Mohammad Tofik has done this\n")
myList = ["Mohammad Tofik", 190905514, 62];
print("The details are = ", myList)
print("Only the name of the student : " + myList[0])

number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number : "))
number3 = int(input("Enter the third number : "))

if (number1 > number2) and (number1 > number3):
	print("Number1 is the greatest number = ", number1)
elif number2 > number3:
	print("Number2 is the greatest number = ", number2)
else:
	print("Number1 is the greatest number = ", number1)