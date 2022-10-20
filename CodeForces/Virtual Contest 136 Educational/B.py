def mainFunc():
    # Given two numbers
    n  = int(input())
    # We have a n rows and m columns
    dArray = list(map(int, input().split()))
    aArray = [0 for i in range(n)]

    aArray[0]=dArray[0]
    def getPossibility(d, a, incomingPos):
        pass
    for i in range(1, n):
        if aArray[i-1]+dArray[i]>=0 and aArray[i-1]-dArray[i]>=0:
            possibility*=2

        if aArray[i-1]+dArray[i]>0:
            aArray[i]=aArray[i-1]+dArray[i]
            possibility=min(possibility, 1)
        elif aArray[i-1]-dArray[i]>0:
            aArray[i]=aArray[i-1]-dArray[i]
            possibility=min(possibility, 2)
    print(aArray,possibility)
t = int(input())

for testcases in range(t):
    mainFunc()