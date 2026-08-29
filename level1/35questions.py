#Question: Get two 3-digit numbers from user. Add the one's and hundred's digits of both
#numbers. Print the sum of all the digits of the number whose sum of one's and hundred's digits
#is bigger.


while True:
    n1 = int(input())
    if n1 >1000 or n1 <99:
        print("enter a 3 digit number")
        continue
    break
while True:
    n2 = int(input())
    if n2 >1000 or n2 <99:
        print("enter a 3 digit number")
        continue
    break
if (((n1%10))+ (n1//100))>((n2%10)+(n2//100)):
    print ((n1%10)+((n1%100)//10)+(n1//100))

else:
        print ((n2%10)+((n2%100)//10)+(n2//100))
