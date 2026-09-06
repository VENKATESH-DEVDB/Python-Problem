#Question: Get a number from user, find the number of digits, and print it.

n = int(input())

def numberofdigit(a):
    count = 0 
    while a> 0:
        a = a// 10 
        count +=1
    return count
print(numberofdigit(n))