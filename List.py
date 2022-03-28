"""
Sequence type
Mutable
heterogenous

list slicing
"""

a = [1,2,3,4,5]

print(a)
print(type(a))	#to find its type

#index related operation - Slicing

a[0] = 100
print("List contains: ",a)
print("Value at index 1: ",a[1])		#to get index value
print("Value at nth index: ",a[-1])		#Nth index
print("Values from 0 to 2: ",a[0:3])	#value at 0 to 2
print("Values from 2 to n: ",a[2:])		#value at 2 to n
print("Values from 0 to 2: ",a[:3])		#value upto 2nd index
print("-----------------------------------------")

#heterogenous

a = [1,True,'Ram',2.5,['a','b','c','d']]

print("List contains: ",a)
print(a,"type is",type(a))
print(a[0],"type is",type(a[0]))
print(a[1],"type is",type(a[1]))
print(a[2],"type is",type(a[2]))
print(a[3],"type is",type(a[3]))
print(a[4],"type is",type(a[4]))
print("Value at 4th index 2nd pos: ",a[4][2])				
print("-----------------------------------------")

#In-build func

a = [1,2,3,4]
print("List contains: ",a)
print("Maximum value in the list: ",max(a))
print("Minimum value in the list: ",min(a))
a.clear()
print("After clear function")
print("List contains: ",a)
print("-----------------------------------------")

a = [1,2,3,4]
print("List A contains: ",a)
b = a.copy()
print("List B contains: ",b)
print("-----------------------------------------")

a = [1,2,3,4,2,3,2,'a','a','b']
print("List contains:	",a)
print("No of times 'a' appear in list: ",a.count('a'))
print("First appearance of 'a' at index: ",a.index('a'))
print("Length of the list: ",len(a))
a.pop(0)											#pop() works based on index
print("after pop funtion at index 0")
print("List contains:	",a)
a.remove('a')										#remove() works based on value
print("after remove funtion on value 'a'")
print("List contains:	",a)
print("-----------------------------------------")

names = ['Arku']
print("List names contains:	",names)
names.append("arun")
names.append("kumar")
names.append("Azhagappan")
print("after append func")
print("List names contains:	",names)

names2 = ["lion","tiger"]
print("List names2 contains:	",names2)

print("after extend func: ")
names.extend(names2)
print("List names contains:	",names)

print("after insert func: ")
names.insert(0,"monika")
names.insert(0,"Anusya")
print("List names contains:	",names)
print("-----------------------------------------")

a = [5,2,4,3,1,8,6,9,99]
print("List contains:	",a)
a.sort()
print("After sort func:	",a)
a.sort(reverse=True)
print("After rev sort func:	",a)

a = ["pineapple","apple","custardapple","orange"]
print("List contains:	",a)
a.sort()
print("sorted list:	",a)
a.sort(reverse=True)
print("reverse sorted list:	",a)
a.sort(key=len)
print("sort based on len:	",a)










