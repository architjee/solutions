n = int(input());
bigList = [];
for i in range(n):
    bigList.append(int(input()));
sortAtIndex = n-1;
while sortAtIndex >= 0:
    maxElement = bigList[0];
    i =0;
    maxIndex = i
    while i<=sortAtIndex:
        if(bigList[i]>bigList[maxIndex]):
            maxIndex = i;
        i+=1
    bigList[maxIndex], bigList[sortAtIndex] = bigList[sortAtIndex], bigList[maxIndex];
    sortAtIndex -= 1;
for x in bigList:
    print(x);