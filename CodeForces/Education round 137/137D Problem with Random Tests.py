import enum


def convStringToVal(str):
    resultant = 0
    twoPow = 1
    for j in range(-1, -1-len(str),-1):
        if str[j]=='1':
            resultant+=twoPow*1
        twoPow*=2
    return resultant

def convValToBinary(val):
    ans = ''
    while val:
        ans += str(val%2)
        val //= 2
    return ans[::-1]
def indexOfFirstZero(s):
    found = False
    for index, x in enumerate(s):
        if x=='0':
            found = True
            return found, index
        
    return found, -1
def mainFunc():
    n = int(input())
    s = input()
    value = convStringToVal(s)
    if not value:
        print(0)
        return
    s = convValToBinary(value);
    
    size = len(s)
    # Now we have s with leading zeros dropped.
    maxOR = value
   
    s1 = s
    found, zeroPos =  indexOfFirstZero(s1)
    if found:
        expectedSizeS2 = size - zeroPos
        # To check for every substring of length expectedSizeS2
        for i in range(0, expectedSizeS2):
            s2 = s[i:i+expectedSizeS2]
            maxOR = max(maxOR, value|convStringToVal(s2))
    else:
        # Means zero is not found, which is good as well.
        pass
    print(convValToBinary(maxOR))

t = 1
for testcase in range(t):
    mainFunc()