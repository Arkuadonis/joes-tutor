"""
Nested for loop

*
**
***
****
*****

"""

for i in range(6):
	for j in range(i):
		print("*",end="")
	print()

print("------------")
"""
*****
****
***
**
*

"""
for i in range(5,0,-1):
	for j in range(i):
		print("*",end="")
	print()
print("------------")
"""
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE
"""
for i in range(5):
	for j in range(65,70,1):
		print(chr(j),end="")
	print()
print("------------")