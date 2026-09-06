#Question: Get a number from user and count the number of zeros in that number.

n = int(input())

def zero (a):
    count = 0 
    while a >  0 :
        c = a %10 
        a = a // 10
        if c == 0:
            count+= 1
    return count
print(zero(n))