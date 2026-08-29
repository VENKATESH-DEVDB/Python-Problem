#Question: Get two 2-digit numbers from user. Print the sum of digits of the biggest number.

while True:
    n1 = int(input())
    if n1 >100 or n1 <9:
        print("enter a 2 digit number")
        continue
    break
while True:
    n2 = int(input())
    if n2 >100 or n2 <9:
        print("enter a 2 digit number")
        continue
    break
if n1>n2:
    print((n1%10)+(n1//10))
else:
    print((n2%10)+(n2//10))