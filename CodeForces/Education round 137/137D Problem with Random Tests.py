def valOf(inp):
    return int(inp, base=2)

def mainFunc():
    n = int(input())
    s = input()
    s = s.lstrip('0')
    if not s:
        # s is empty means we should throw zero at the system.
        print(0)
        return
    zeroPos = -1
    for index, value in enumerate(s):
        if value=='0':
            zeroPos=index
            break
    if zeroPos==-1:
        
        # That means there is no zero, which is a good thing because we can simply print s and be done with.
        print(s)
        return
    expectedS2Size = len(s)-zeroPos
    
    maxOrPossible = valOf(s)
    for i in range(0, len(s)-expectedS2Size):
        maxOrPossible = max(maxOrPossible, valOf(s[i:i+expectedS2Size])|valOf(s))   
    print(bin(maxOrPossible).replace('0b', '')) 
    return
t = 1
for testcase in range(t):
    mainFunc()