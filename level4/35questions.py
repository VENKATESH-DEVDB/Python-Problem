#Question: Get two numbers from the user and find their LCM.

def hcf (a,b):
    while b > 0: 
        a,b  = b , a%b 
    return a 
def Lcm (a,b):
    lcm = ( (a*b)/hcf(a,b))
    return lcm
def user_input():
    v1,v2 = map(int,input().split())
    return Lcm(v1,v2)
print(int(user_input()))