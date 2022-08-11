from functools import cmp_to_key

n = int(input())
bigList = list(map(int, input().split()))


def customCompare(a, b):
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    elif a[0] == b[0]:
        if a[1] < b[1]:
            return -1
        elif a[1] > b[1]:
            return 1
        else:
            return 0


d = {}
for x in bigList:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
totalUniqueNumbers =d.keys()
valuesKeyMapping = []

for x in totalUniqueNumbers:
    valuesKeyMapping.append([d[x], x])
valuesKeyMapping.sort(key=cmp_to_key(customCompare))
for value, key in valuesKeyMapping:
    for x in range(value):
        print(key, end=" ")
