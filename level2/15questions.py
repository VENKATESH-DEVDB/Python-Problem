#Question: Write a program to get a number from the user. If the first digit is even, print
#the same number. If the first digit is odd, subtract 1 from the first digit and print the
#number.

n = int(input())
count = 0 
ans = n 
while n > 0:
    n = n // 10 
    count = count + 1
else :
    if ((ans//(10**(count-1))) )%2 == 0:
        print (ans)
    else :
        print (ans - (10**(count-1)))