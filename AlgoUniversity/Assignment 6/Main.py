# P20 UNION.
n, m = map(int, input().split());
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))
bigSet = set()
for x in arrayA:
    bigSet.add(x)
for x in arrayB:
    bigSet.add(x)
bigList = list(bigSet)
bigList.sort()
for y in bigList:
    print(y, end=' ')
