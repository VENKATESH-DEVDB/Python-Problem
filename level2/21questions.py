#Question: Write a program to get a number from the user and print the total number of
#digits that are odd.

n = int(input())
count = 0 
while n >0:
    c = n %10 
    n = n //10
    if c %2 != 0:
        count += 1 
else :
    print(count)