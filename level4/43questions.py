#Question: Get a string and check whether it is a valid number.
 
n = input()
bol = True
try :
    n = int(n)
except ValueError :
    print("not valid")

if bol :
    print("valid")