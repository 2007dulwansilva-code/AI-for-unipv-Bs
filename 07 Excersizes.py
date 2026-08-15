#palindrome problem
def is_palindrome(x):
    if x[:] == x[::-1] :
        return True
    else:
        return False

#ans = is_palindrome(input("enter word"))
#print(ans)

#Write a function called is_abecedarian that returns True if
# the letters in a word appear in alphabetical order(double
# letters are ok).

def is_abecedarian (x):
    leng = len(x)
    for i in range(leng-1):
            if x[i] > x[i+1]:
                return False
    return True

print(is_abecedarian("agh"))
        
#replace string
def repl(line):
    line.replace("banana","Banana")

#replacing element on string

def retouch (x,y,z):
     oldt = x
     newt = oldt[:y-1] + z + oldt[y+1:len(oldt)]
     return newt

print (retouch("blahblah",4,"a"))


#excersize 3

def repl (x,y):
     t1 = x
     t2 = y
     newt = ""
     for i in range(len(t1)):
          if t1[i] == t2[i]:
               newt = newt + "*"
          else:
               newt = newt + "-"
     return newt

print( repl("baaa","blaa") )
               
#Excersize 4
def conc (x,y):
     upp = x.upper()
     lowe = x.lower()
     newt = "" 
     for i in range(len(x)):
          if y[i] == "+":
               newt = newt + upp[i]
          elif y[i] == "-":
               newt = newt + lowe[i]
     return newt
print(conc("NigGra","++-+--"))

#Excersize 6
def rem (x,y):
     newt = ""
     for i in range(len(x)):
          if y[i] == "+":
               newt = newt + x[i]
     return newt

print(rem("apple","++--+"))

#Excersize 7
def checkchar (x,y):
     for i in range(len(x)):
          for j in range(len(y)):
               if x[i] == y[j]:
                    return True
     return False
print(checkchar("apple","humn"))

#Excersize 10
reader = open("words.txt")

for line in reader : 
     word = line.strip()
     if is_abecedarian(word):
          print(word)
