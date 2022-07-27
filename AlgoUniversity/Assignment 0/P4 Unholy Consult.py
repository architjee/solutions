n, m = map(int, input().split())
narr = []
marr = []
for x in range(n):
    length, speed = map(int, input().split())
    narr.append([length, speed])
narr.append([0,0])
for x in range(m):
    length, speed = map(int, input().split())
    marr.append([length, speed])
marr.append([0,0])
pn = 0
pm = 0
ans = 0 #max violation is zero initially.
tx = narr[0][0]
ty = marr[0][0]
while pn < n and pm < m:
    ans = max(ans, marr[pm][1]-narr[pn][1])
    if tx < ty:
        pn += 1
        tx += narr[pn][0]
    elif tx > ty:
        pm += 1
        ty += marr[pm][0]
    else:
        pn += 1
        pm += 1
        tx += narr[pn][0]
        ty += marr[pm][0]
print(ans)