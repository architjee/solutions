x, y , a,b = map(int, input().split())
ans = min( abs(x-y), min(abs(x-a)+abs(y-b), abs(x-b)+abs(y-a)))
print(ans)