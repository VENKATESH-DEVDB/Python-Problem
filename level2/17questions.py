#Question: Write a program to get a number from the user, print whether that number is
#prime, and check whether the sum of its digits is equal to 14.

n = int(input())
ans = ""
if n ==1 or n ==1 :
    print("enter number greater that 1 ")
elif n == 2:
    ans = "Prime"
elif n %2==0:
    ans = "Not Prime"
else :
    for i in range (3,int((n**0.5))+1):
        if n %i == 0 :
            ans = "Not Prime"
            break 
    else :
      ans = "Prime"
total =     0 
while n > 0 :
    c= n %10 
    n = n//10
    total = total  + c 
    if total == 14:

        print (ans , "the sum of digit is 14")
        break 
else :
    print(ans , " the sum of digit is not 14")