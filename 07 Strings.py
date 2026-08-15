#store the string in a variable
fruit = "apple"
#length
leng = len(fruit)
#first letter
letter = fruit[0]
# An empty string is written as ""
#we can provide a negative index where the rightmost side is indexed with -1
last = fruit[-1]

#we can slice a string using the [start:stop:index]
print(fruit[:3]) # first three letters
print(fruit[1::2]) # Every even character
print(fruit[1:1]) # Empty string.
print(fruit[:]) # The whole string

# We can reverse the order of string characters
print(fruit[::-1])

#A string is immutable, meaning we cannot change an individual character
#However it can be re assigned
#Relational operators work on strings
#Among str methods:

#str.capitalize()
#str.lower()
#str.upper()
#str.endswith()
#str.startswith()
#str.find()
#str.index()
#str.split()
#str.strip()
#str.isalpha()
#str.isdecimal()
#str.isdigit()
#str.isnumeric()
#str.islower()
#str.isupper()
#str.join()
#str.replace()
#str.count()
