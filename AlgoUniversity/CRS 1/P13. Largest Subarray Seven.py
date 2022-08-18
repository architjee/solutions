# This question seems like Prefix sum might help us calculated all of it.
n = int(input())
array = [0] * n
for i in range(n):
    array[i] = int(input())
prev = array[0]
prefixArray = [array[0]]
d = {}
ans = 0
for i in range(n):
    prefixAtR = prefixArray[i]
    if prefixAtR:
        pass
print(ans)
