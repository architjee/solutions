def mainFunc():
    n = int(input())
    if not n:
        print(0)
        return
    count = 0
    while n:
        n = n&(n>>1)
        count+=1
    print(count)
t= int(input())
for testCase in range(t):
    mainFunc()