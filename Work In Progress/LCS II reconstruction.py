t = input()
s = input()
n= len(s)
m = len(t)
dp= [[0 for x in range(n+1)] for y in range(m+1)]
for y in range(m+1):
    for x in range(n+1):
        if x==0 or y==0:
            continue
        if s[x-1]==t[y-1]:
            dp[y][x]= 1 + dp[y-1][x-1]
        else:
            dp[y][x]= max(dp[y-1][x], dp[y][x-1])

         
# x = n
# y = m
# result = []
# while y>0 and x>0:
#     if s[x-1]==t[y-1]:
#         result.append(s[x-1]+'') ## Same as appending t[y-1]
#         x-=1
#         y-=1
#     else:
#         if dp[y-1][x]> dp[y][x-1]:
#             y-=1
#         else:
#             x-=1

# print(''.join(reversed(result)))
print(dp[-1][-1])