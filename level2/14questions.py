#Question: Write a program to get a number from the user and interchange the first and
#last digits, then print the result.


n = int(input()) 
output  = 0
count = 0 
ans = n
while n > 0 :
    n = n//10
    count = count + 1
else:
    
   first_digit = (ans//(10**(count -1)))
   last_digit = ans %10 
   num = (ans%(10**(count -1)))
   num = num //10
   output = ((num + (last_digit *(10**(count-2)))) *10 )+ first_digit
print(output)