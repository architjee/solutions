array = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSoFar = 0
ans = 0
for x in array:
    ans = max(x, maxSoFar+x)
    if ans>maxSoFar:
        maxSoFar = ans
print(ans)