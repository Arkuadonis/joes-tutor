i = 1
while i <= 10 :
	print(i)
	i += 1

print("---------------------")
# To print odd no
i = 1
while i <= 20:
	print(i)
	i += 2

print("---------------------")
#Even
i = 1
while i <= 20:
	if i % 2 == 0:
		print(i)
	i += 1

print("---------------------")
#Continue stmt - odd
i = 1
while i <= 20:
	if i%2 == 0:
		i += 1
		continue
	print(i)
	i += 1

print("---------------------")
#Break stmt 
i = 1
while i <= 20 :
	if i == 7:
		break
	print(i)
	i += 1
