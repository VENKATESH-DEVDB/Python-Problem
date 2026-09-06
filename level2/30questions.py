#Question: Write a program to get two numbers from the user and print the HCF of those
#numbers.



a = int(input())
b = int(input())

while b >0:
    a, b = b , a%b 
print(int(a))