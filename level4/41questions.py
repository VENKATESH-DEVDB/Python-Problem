#Question: Get an integer and print each digit as a character, one character per line.

n = int(input())
for i in range(len(str(n))):
    print(str(n)[i])
