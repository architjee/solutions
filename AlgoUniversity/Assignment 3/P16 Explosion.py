# P16 : Explosion.
n = int(input())
bigList = list(map(int, input().split()))
bigList.sort()
jd = 0
ans = 0
for i in range(0, n):
    jd = 1
    startIndex = i
    print(startIndex)
    for j in range(i + 1, min(i + 1 + jd, n)):
        if bigList[j] <= (bigList[startIndex] + jd):
            startIndex = j
            jd += 1
            ans = max(ans, j)
        else:
            break
secondAns = 0
for i in range(n-1, -1, -1):
    jd = 1
    startIndex = i
    print(startIndex)
    for j in range(i - 1, min(-1,i-jd-1), -1):
        if (bigList[startIndex] + jd) >= bigList[j]:
            startIndex = j
            jd += 1
            secondAns = max(secondAns, j)
        else:
            break
print(secondAns)
