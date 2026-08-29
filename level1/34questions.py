#Question: Get two 3-digit numbers from user. Print the difference between the one's digit and
#hundred's digit of the number whose ten's digit is bigger than the other number's ten's digit.


while True:
    n1 = int(input())
    if n1 >1000 or n1 <=99:
        print("enter a 3 digit number")
        continue
    break
while True:
    n2 = int(input())
    if n2 >1000 or n2 <=99:
        print("enter a 3 digit number")
        continue
    break
if ((n1%100)//10)> ((n2%100)//10):
    if ((n1%10)>(n1//100)):
        print((n1%10)-(n1//100))
    else:
        print((n1//100)-(n1%10))
else:
    if ((n2%10)>(n2//100)):

        print((n2%10)-(n2//100))
    else :
        print((n2//100)-(n2%10))