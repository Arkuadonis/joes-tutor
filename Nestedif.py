"""

a)3 Marks as ip
b)find total,avg,result.
c)grade:
if pass,then 
A for 90-100
B for 80-89
C for 70-79
D for 69-35

"""

m1 = int(input("Enter mark-1: "))
m2 = int(input("Enter mark-2: "))
m3 = int(input("Enter mark-3: "))

total = m1+m2+m3
avg = total/3

print("Total: ",total)
print("Average: ",avg)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
	print("Result: Pass")
	if avg >= 90 and avg <= 100:
		print("Grade: A")
	elif avg >= 80 and avg <= 89:
		print("Grade: B")
	elif avg >= 70 and avg <= 79:
		print("Grade: C")
	elif avg >= 35 and avg <= 69:
		print("Grade: D")
else:
	print("Result: Fail")
