a = int(input())
b = int(input())
c = int(input())
possibilities = [a+b+c, (a*b)+c, a*(b+c), a*b*c, (a+b)*c, a+(b*c)]
maxVal = max(possibilities)
print(maxVal)