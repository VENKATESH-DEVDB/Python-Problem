    #Question: Get a two-digit number from user and print the ten's digit.#
count = 0 
while True  :
    
    n = int(input())
    if n > 100 or n <10:
        print( " enter a 2 digite number")
        continue
    break 
while n >0:
    a = n %10 
    count = count +1 
    if count == 2 :
        print(a)
        break 
    n = n//10
 