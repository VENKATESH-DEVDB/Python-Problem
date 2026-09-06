#Question: Get a number from user and check whether the sum of digits is 14, then print 
# the result.

n = int(input())
def function (a):
    total = 0 
    while a > 0:
        total  += a%10
        a = a // 10 
    if total == 14 :
        return f"the sum of the digit is 14"
    else :
        return " the sum of the digit is not 14"
print(function(n))