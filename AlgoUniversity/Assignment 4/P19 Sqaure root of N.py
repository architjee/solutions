n= int(input())
low = 0
high = n
steps = 150
def predicate(x, n):
    if(x*x < n):
        return 0
    return 1
while steps:
    mid = (low+high)/2
    if(predicate(mid,n)==0):
        low = mid
    else:
        high = mid
    steps -=1
print(mid)