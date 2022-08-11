n = int(input())
bigList = list(map(int, input().split()))
prefix = []
cumulativeSum = 0
for x in bigList:
    cumulativeSum += x
    prefix.append(cumulativeSum)
mainSet = set()
flag = False
for x in prefix:
    if x in mainSet:
        flag = True
    mainSet.add(x)
if(flag==True):
    print("YES")
else:
    print("NO")
