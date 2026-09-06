#Question: Write a program to get a number from the user and print the total number of
#single-digit perfect square numbers in the number.

n = int(input())
squar = [1,4,9,0]
count  = 0
while n >0:
    c = n %10 
    n = n//10
    if c in squar:
        count  +=1
else : print (count)