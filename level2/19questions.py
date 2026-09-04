#Question: Write a program to get a 4-digit number from the user and print whether the
#middle two digits form a prime number.

while True :
    n = int(input())
    if n > 10000 or n < 999:
        print("Enter a 4 digite number")
        continue
    else:
        break

middle_num = (n//10)%100

if middle_num > 2 :
    if middle_num%2 == 0 :
        print("not prime")
    else :
        for i in range (3,int((middle_num**0.5))+1):
            if middle_num %i == 0 :
                print("not prime")
                break 
        else:
            print("Prime")
else:
    print ("the middle two number are ",middle_num,"neither prime")