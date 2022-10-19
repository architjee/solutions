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
def mainFunc():
    n = int(input())
    s = input()
    value = convStringToVal(s)
    s = convValToBinary(value);
    # Now we have s with leading zeros dropped.
    solved = False
    for index, val in enumerate(s):
        if val=='0':
            # We have found our position.
            print("The index we are getting this is", index)
            print(convValToBinary(value | (value>>index)))
            solved = True
            break
    if not solved:
        print(s)
t = 1
for testcase in range(t):
    mainFunc()