n = int(input())
arr = list(map(int, input().split()))
stk = []
result = []
# Consider an invariant
# That elements in the stack will always be in the will always be of the form
# 10 8 7 6 5
for x in arr:
    if not stk:
        stk.append(x)
        result.append(-1)
    else:
        while stk and stk[-1]<=x:
            stk.pop()
        if not stk:
            result.append(-1)
        else:
            result.append(stk[-1])
        stk.append(x)
print(*result, sep=' ')
