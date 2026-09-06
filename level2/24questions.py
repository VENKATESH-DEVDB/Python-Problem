#Question: Write a program to get a number from the user and print the total number of
#two-digit perfect square numbers in the number.

n = int(input())

count  = 0
while n >0:
    c = n %100
    n = n//10
    two_digit = c ** 0.5
    if two_digit%1 == 0:
        count  = count + 1
else : print (count)