#Dictionaries
#A dictionary is similar to a list but it has a key for each index
#Empty dictionary
eng2ita = {}
enge2ita = {"one" : "uno", "two" : "dos"}

#copying a dictionary 
cop = dict(eng2ita)

#In operator can be used to check if a key is in the dict
#we can use values to check for an element in the dict
vals = eng2ita.values()
"one" in vals

#Return the list of reversible words
def reversibles(words): #assigning name of fun
    rev = [] #new list to add the reversible words
    for w in words : # for each word in the dictionary words
        if w[::-1] in words : #if exists its inverse in the same dictionary
            rev.append(w) #add the word to the new list
    return rev

#Searching in dicts
#Note that using dicts has faster processing time than lists

words_dict = {} #creating empty dictionary
for w in open("words.txt"): #going through every line of the file
    words_dict[w.strip()] = 1 #we strip newline characters
    reversibles(words_dict)

