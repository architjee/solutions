def mainFunc():
    n = int(input())
    if not n:
        print(0)
        return
    # We can get binary representation with bin I guess
    binaryString = bin(n).replace('0b', '')
    prev = 0
    i = 0
    highCount = 1
    while i<len(binaryString):
        ele = binaryString[i]
        if ele=='1':
            j = i+1
            highCount = max(highCount, j-i)
            while(j<len(binaryString) and binaryString[j]=='1'):
                j+=1
                highCount = max(highCount, j-i)
        i+=1
    print(highCount)
t= int(input())
for testCase in range(t):
    mainFunc()