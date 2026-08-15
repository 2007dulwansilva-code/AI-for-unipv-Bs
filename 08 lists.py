#Lists
#A list is a sequence of values
len(["blah",2,3,4])
empty = []
#Lists are mutable
# the IN operator works here
numbers = [1,2,42,33,44]
42 in numbers

for n in numbers:
    print(n)

#we can concatenate two lists with + or repeat with *

numbers[1:3]=[3,3]
print (numbers)

#list.append() can be used to add a new element to the end of the list
#list.extend() to add one of more elements to a list
#list.sort() to sort the elements in a list
#we can use sum to sum the list

#list.pop(i) removes the ith element and returns it
#del t[3] deletes the element with no return
#list.remove("a") removes any element a, no return


#WHILE statments
def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("blastoff!")

#continue terminates the current iteration and moves to the next
#break concludes the iteration
