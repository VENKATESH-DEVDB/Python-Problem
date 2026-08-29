#Question: Get a two-digit number from user and print sum the digits.#
two_sum = 0 
while True  :
    
    n = int(input())
    if n > 100 or n <=9:
        print( " enter a 2 digite number")
        continue
    break 
while n>0:
    c= n%10
    two_sum = two_sum +c
    n=n//10
else :
    print(two_sum)
    