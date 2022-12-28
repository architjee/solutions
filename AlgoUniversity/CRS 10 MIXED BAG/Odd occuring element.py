n = int(input())
arr = list(map(int, input().split()))
culprit = 0
for x in arr:
    culprit = culprit ^ x
print(culprit)