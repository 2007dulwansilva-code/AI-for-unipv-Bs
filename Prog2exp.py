openers = ["(","[","{"]
closers = [")", "]", "}"]

def matches(open,close):
    return openers.index(open) == closers.index(close)

def parcheck(string) :
    s = Stack()
    for symbol in string :
        if symbol in openers:
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    return False
if s.isEmpty():
    return True
return False
