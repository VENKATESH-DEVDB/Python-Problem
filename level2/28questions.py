#Question: Write a program to get two numbers from the user and print the LCM of those
#numbers

a = int(input())
b = int(input())

v1,v2 = a,b
while b >0:
    a, b = b , a%b 
lcm = (v1*v2)/a
print(int(lcm))