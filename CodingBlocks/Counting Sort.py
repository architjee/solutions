bigList = [0 for _ in range(1000001)]
n= int(input());
line = map(int, input().split());
for x in line:
    bigList[x] += 1;

for x in range(0, 1000001):
    for _ in range(bigList[x]):
        print(x,end=' ')
        bigList[x]-=1;
    