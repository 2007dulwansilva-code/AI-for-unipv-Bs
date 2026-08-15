#functions
#INT converts any value to integer if possible
int("32")
int(-9.8)
#FLOAT converts any value to a float value
float(32)
float("3.33")

#adding new functions
#syntax is def <function_name> (): 

def print_lyrics():
    print("blah blah")
    print("black sheep")
#we call the function like this
print_lyrics()

#we can re use these functions within another function
def repeating ():
    print_lyrics()
    print_lyrics()

repeating()

#repeatitions
for i in range(3) :
    print(i, "blah")
#note that i starts with 0 and before 3, therefore i is 0,1,2


