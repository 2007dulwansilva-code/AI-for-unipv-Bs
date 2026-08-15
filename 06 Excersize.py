#finding in between
def is_between (x,y,z) :
    if (x<y):
        if(y<z):
            return True
        else:
            return False
    else:
            return False
    
print(is_between(1,2,3))
print(is_between(11,2,3))
print(is_between(12,22,23))

#recursive natural power
def iter_pow (a,n) :

    p = 1
    for i in range(n):
        p = a * p
    return p

print(iter_pow(3,2))

#Ackermann function

def A(n,m) :
     if m == 0 :
          return n+1
     elif n == 0 :
          return A(m-1,1)
     else:
          return A((m-1),(A(m,n-1)))

ans = A (1,5)
print(ans)