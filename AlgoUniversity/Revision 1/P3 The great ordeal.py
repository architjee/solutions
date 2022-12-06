arr = list(map(int, input().split()))
arr.sort()
a,b,c = arr[0], arr[1], arr[2]
d1 = b-a
d2 = c-b
minimum_moves ,maximum_moves = 0,0
if d1==1 and d2==1:
    minimum_moves , maximum_moves = 0, 0
else:
    
    if min(d1,d2)==1 and max(d1, d2)==2:
        minimum_moves = 1
        maximum_moves = 1
    elif min(d1, d2)==2:
        minimum_moves = 1
    else:
        minimum_moves = min(2, max(d1, d2)-1)
    maximum_moves = max(d1, d2)-1
print(minimum_moves)
print(maximum_moves)