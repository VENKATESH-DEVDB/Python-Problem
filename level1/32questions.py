#uestion: Get two 2-digit numbers from user. If the sum of the numbers is less than 100, then
#print the sum, otherwise print the difference

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
if (n1 + n2)>100:
    if n1>n2:
        print(n1-n2)
    else:
        print(n2-n1)
else :
    print(n1+n2)
