#Question: Get two numbers from user and compare them. If they are the same, print
#Same; otherwise print Not Same.


n = int(input())
m = int(input())
def same(a,b):
    if a == b :
        return "same"
    else:
        return "not same "
print(same (n,m))