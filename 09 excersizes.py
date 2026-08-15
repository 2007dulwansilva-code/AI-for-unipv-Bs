#Letter frequency histogram
#counting each time a letter appears
def wcount(word):
    d = dict()
    for i in word:
        if word not in d :
            d[word] = 1
        else:
            d[word] += 1
    return d

