#Question: Get a number from user and subtract 5 from that number if the number's ten's position
#digit is odd, then print the result. 

n = int(input())
c = n %100 
c = c//10
odd = [3,5,7,9]
bol = c in odd
while bol:

    print(n-5)
    break 
else:
    print(n)
