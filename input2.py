 # input() always takes as string

A = input("Enter the value of A: ")
B = input("Enter the value of B: ")
C = A+B
print("A + B = ", C)

"""

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
C = A+B
print("A + B = ", C)

A = float(input("Enter the value of A: "))
B = float(input("Enter the value of B: "))
C = A+B
print("A + B = ", C)

------------------ Output

python3 input2.py 
Enter the value of A: 45
Enter the value of B: 46
A + B =  4546

python3 input2.py
Enter the value of A: 45
Enter the value of B: 46
A + B =  91

python3 input2.py
Enter the value of A: 45.5
Enter the value of B: 46.2
A + B =  91.7
"""