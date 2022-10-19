def mainFunc():
    # n is the no. of boxes
    n = int(input())

    # Given that 1 is lid, 0 is not lid.
    lidState = input()
    lidState = '0'+lidState;

    boxContents = [0]+list(map(int,input().split()))
    ans = 0
    i=0
    while i<=n:
        mn = boxContents[i]
        sm = boxContents[i]
        j = i+1
        while j<=n and lidState[j]=='1':
            mn = min(mn, boxContents[j])
            sm += boxContents[j]
            j+=1
        ans += sm - mn
        i=j
    print(ans)
# Given t test cases
t = int(input())
for testcase in range(t):
    mainFunc()