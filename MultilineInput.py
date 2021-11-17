Name=["Arun","Pandian","Riyas"]  #Should be string for join
print(",".join(Name))

Employee=[]
print("Enter the multilines : ")

while True:
	word=input()
	if word:
		Employee.append(word)

	else:
		break

print(Employee)
print('\n'.join(Employee))

"""
python3 MultilineInput.py			//execution

Arun,Pandian,Riyas					//input
Enter the multilines : 
arun from theni. 
pandian from madurai.
riyas from sivagangai.
									//output

['arun from theni.', 'pandian from madurai.', 'riyas from sivagangai.']
arun from theni.
pandian from madurai.
riyas from sivagangai.