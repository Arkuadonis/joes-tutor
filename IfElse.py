"""
Program to check vote eligibility
"""

name = input("Enter the name: ")
age = int(input("Enter the age: "))

if age >= 18:
	print(name,"age is ", age,", Eligible for voting")
else:
	print(name,"age is", age,", Not eligible for voting")