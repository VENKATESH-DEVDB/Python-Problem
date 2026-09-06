#Write a program to print the biggest 4-digit number which is divisible by 7 and
#9.
n = 9999
while n >= 1000:
    if n % 7 == 0 and n %9 == 0 :
        print(n)
        break 
    n -=1