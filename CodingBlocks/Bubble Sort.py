n = int(input());
bigList = []
for i in range(n):
    bigList.append(int(input()))
for i in range(0, len(bigList)-1):
    for j in range(i+1, len(bigList)):
        if(bigList[i]>bigList[j]):
            bigList[j],bigList[i] = bigList[i], bigList[j]
for x in bigList:
    print(x)