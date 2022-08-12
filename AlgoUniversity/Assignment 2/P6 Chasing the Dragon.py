n = int(input())
distancesArr = map(int, input().split())
# Calculation of prefix Sum array.
prefix = []
prev = 0
for x in distancesArr:
    prev += x
    prefix.append(prev)
# print(prefix)
k = int(input())
lastPos = 0
for _ in range(k):
    t, d = map(int, input().split())
    # Since we wanna travel d distance and in t direction.
    distance = ((t*d)%n) + n
    # It means v might have extra n added to it.
    nextPos = (lastPos+distance)%n
    u, v= min(nextPos, lastPos), max(nextPos, lastPos)
    rightAns = prefix[v] - prefix[u]
    ans = min(rightAns, prefix[-1]-rightAns)
    print(ans)
    lastPos = nextPos