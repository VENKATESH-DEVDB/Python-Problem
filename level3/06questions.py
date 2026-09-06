#Question: Get a number from user and reverse that number.

n = int(input())

def rev (a):
    revers = 0 
    while a >  0 :
        c = a %10 
        a = a // 10
        revers   = revers*10 + c 
    return revers
print(rev (n))