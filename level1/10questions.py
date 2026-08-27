#Question: Get a three-digit number from user and print the ten's digit.#
count = 0 
while True  :
    
    n = int(input())
    if n > 1000 or n <100:
        print( " enter a 3 digite number")
        continue
    break 
while n >0:
    a = n %10 
    count = count +1 
    if count == 2 :
        print(a)
        break 
    n = n//10