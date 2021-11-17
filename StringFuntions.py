s = "Python Programming language"
print(s)
print(type(s))

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("n"))
print(s.endswith("ge"))
print(s.find("g"))
print(s.find("g",11)) #after 11th position
print(s.replace("P","9"))

#boolean string fun
print(s.islower())
print(s.isupper())
s="123arun"
print(s.isalnum())
s="arun"
print(s.isalpha())

#split fun
s= "he\nis\ngood"
print(s.splitlines())
print(s.splitlines(True)) #True 'T' must be caps
s="arun is from India"
print(s.split())		#default delimiter space
s="arun,pandian,riyas"
print(s.split(","))		#changing delimters as ,

#len fun and strip fun
s="       arunkumar.        "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))

""" ----------OUTPUT-------

python3 StringFuntions.py


Python Programming language
<class 'str'>
PYTHON PROGRAMMING LANGUAGE
python programming language
Python programming language
Python Programming Language
3
True
10
17
9ython 9rogramming language
False
False
True
True
['he', 'is', 'good']
['he\n', 'is\n', 'good']
['arun', 'is', 'from', 'India']
['arun', 'pandian', 'riyas']
25
10
18
17
