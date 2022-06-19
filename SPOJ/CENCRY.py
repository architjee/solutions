import sys
vowelArray     = "aeiou"
consotantArray = "bcdfghjklmnpqrstvwxyz"
t = int(sys.stdin.readline())
import string
d2 = dict.fromkeys(string.ascii_lowercase, 0)
# print(d)
for _ in range(t):
    def isVowel(c):
        if c in ('a','e','i','o','u'):
            return True
        return False

    result = []
    original = input()
    d = {}
    for c in original:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
        k = d[c]
        if isVowel(c):
            index = vowelArray.find(c)
            result.append(consotantArray[((k-1)*5+index)%21])
        else:
            index = consotantArray.find(c)
            result.append( vowelArray[((k-1)*21+index)%5])
             
    print("".join(result))