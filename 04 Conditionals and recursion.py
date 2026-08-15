#Conditionals and recursion
#Boolean expressions
#A boolean expression is either true or false
type(True)
type(False)
x = 2
y= 3
type(x == y)
type(x != y)
type(x < y)
type(x > y)
type(x <= y)
type(x >= y)

#logical operators and or not
#precedence not and or

#conditional excecution
if x > 1 :
    print("greater than 1")
else : 
    print("less than 1")

#recursion

def countdown(n) :
    if n <= 0 :
        print("kaboom!")
    else: 
        print(n)
        countdown(n-1)

countdown(3)