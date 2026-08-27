#Question: Get a two-digit number from user and print the one's digit#
while True  :
    
    n = int(input())
    if n > 100 or n <10:
        print( " enter a 2 digite number")
        continue
    break 
print ( n %10)