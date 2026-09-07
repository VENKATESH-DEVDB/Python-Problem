#Question: Get a number from the user and print its reverse.

n = int(input())
  
rev =  0 
while n > 0 :
     c = n %10 
     n = n // 10 
     rev = rev * 10 + c  
else:
     print(rev )