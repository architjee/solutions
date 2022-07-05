# Program for Chewbacca coding blocks problem Passing partial test cases
bigString = list(input());
for i in range(len(bigString)):
    x = bigString[i]
    if x>='5':
        bigString[i] = str(9-int(x))
result = int("".join(bigString))
print(result)