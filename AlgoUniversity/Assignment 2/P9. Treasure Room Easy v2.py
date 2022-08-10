n, w = map(int, input().split())
bigList = list(map(int, input().split()))
idxArray = [-1] * 1000005
for index, value in enumerate(bigList):
    idxArray[value] = index
possible = False

for i in range(0, len(bigList)):
    if (bigList[i] < w) and not possible:
        wrem = w - bigList[i]
        for j in range(i + 1, len(bigList)):
            if bigList[j] < wrem:
                wremaining = wrem - bigList[j]
                if idxArray[wremaining] != -1 and idxArray[wremaining] != j and idxArray[wremaining] != i:
                    print(i + 1, j + 1, idxArray[wremaining]+1)
                    possible = True
                    break
if not possible:
    print(-1)
