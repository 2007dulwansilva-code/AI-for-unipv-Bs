#Tuples are similar to lists
#A tuple object is a sequence of values, immutable

#Tuple syntax 
t = ("a","b")

#a single element tuple is represented with a final comma
b = "a",

#creating an empty tuple 
c = tuple()
# or c = ()
#To create a tuple from a sequence

d = tuple("humans")
print (d)
#Gives ("H","u","m"...)
#Each element of the sequence becomes that of a tuple
#Works also with dict where keys are considered

#Indexing, concatenating, duplication works as normal
#We can add sorted

e = sorted(d)
print(e)
f = tuple(reversed(d))
#remember to add tuple when reversing

print(f)
#a tuple is immutable
#Although replacement is possible

f = ("a",) + f[1:]
print(f)

#We can use tuples for comparisons

#tuple can be used as a return value
g = divmod(7,4)
#returns g  as (1,3)
quot, rem = divmod(7,3)
#quot becomes 1 and rem becomes 3

#applying the star * to the parameter packs the argument as a tuple
def printall (*args):
    print(args)

printall(2,"a",True)

#the opposite of packing is unpacking
t = (7,3)
divmod(*t)
#returns(2,1)
# zip () is a built in function that takes two or more sequences and interleaves them, for example zip(s,t)
#for s = "abc" and t = [0,1,2] makes them pairs of tuples

for pair in zip(s,t) :
    print(pair)

# A zip can be transformed into a list of tuples
#Upto page 9 done