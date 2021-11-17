#While else and For else

i = 1
while i <= 10:
	if i == 7:
		i += 1
		continue
	print(i)
	i += 1	
else:
	print("While loop executed successfully")

i = 1
while i <= 10:
	if i == 7:
		i += 1
		break
	print(i)
	i += 1	
else:
	print("While loop executed successfully")