    #Question: Get a two-digit number from user and print the ten's digit.#
n = int(input())
count = 0 
while n >0 :
    a = n %10
    count = count +1 
    if count == 2 :
        print(a)
        break 
    n = n //10 