#Question: Write a program to get a number from the user and print whether that number
#is prime or not.

n = int(input())
if n ==1 or n ==1 :
    print("enter number greater that 1 ")
elif n == 2:
    print("prime")
elif n %2==0:
    print("not prime")
else :
    for i in range (3,int((n**0.5))+1):
        if n %i == 0 :
            print("not prime")
            break 
    else :
        print("prim")