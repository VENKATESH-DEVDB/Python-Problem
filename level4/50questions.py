#Question: Get two numbers of up to 50 digits, perform addition, and print the result.

Max = 50 
while True:
    n1 = input()
    if len(n1) > Max:
        print(" enter digit only up to 50 digit ")
        continue
    break

while True:
    n2 = input()
    if len(n2) > Max:
        print(" enter digit only up to 50 digit ")
        continue
    break
print (n1+n2)