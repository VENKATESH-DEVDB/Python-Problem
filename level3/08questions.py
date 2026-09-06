#Question: Get a number from user and check whether its digits are in ascending order.


n = int(input())

def assending(a):
    bol = False
    while a> 0 :
        last = a %10
        a = a//10
        last_before = a %10
        if last > last_before:
            bol = True
        else :
            return " No"
    else :
        if bol :
            return "Yes"
print(assending(n))