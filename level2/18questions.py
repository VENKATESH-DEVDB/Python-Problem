#Question: Write a program to get a number from the user and print whether the last two
#digits form a prime number

n = int(input())

last_two_digit = n%100
if last_two_digit>2:
    if last_two_digit%2 == 0:
        print ("not prime")
    else:
        for i in range(3,int((last_two_digit**0.5))+1):
            if n %i == 0 :
                print ("not prime")
                break 
        else :
            print("prime")

else :
    print("the last 2 digit is ",last_two_digit,"not  prime")     