#Question: Get a three-digit number from user and print the one's digit.#\
count = 0 
while True  :
    
    n = int(input())
    if n > 1000 or n <=99:
        print( " enter a 3 digite number")
        continue
    break 

print(n%10)