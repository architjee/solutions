n, m = map(int, input().split());
bigList = []
for _ in range(n):
    bigList.append(list(map(int, input().split())))
col = 0;
row = 0;
counter = True;
while col < m:
    if(counter):
        i=0
        while i<n:
            print(bigList[i][col], end=', ')
            i+=1
    else:
        i=n-1;
        while i>=0:
            print(bigList[i][col], end=', ')
            i-=1
        
    counter = not counter
    col +=1
print("END")