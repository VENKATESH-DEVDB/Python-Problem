#Question: Get a three-digit number from user and print sum the digits.#
three_sum = 0 
while True  :
    
    n = int(input())
    if n > 1000 or n <=99:
        print( " enter a 3 digite number")
        continue
    break 
while n>0:
    c= n%10
    three_sum = three_sum +c
    n=n//10
else :
    print(three_sum)
    