# Program for coding blocks question String Sort
n = int(input());
bigList = []
for i in range(n):
    bigList.append(input());
# Implementing bubble sort.
for i in range(n):
    for j in range(i+1, n):
        if(bigList[j].find(bigList[j-1])!=-1):
            bigList[j] , bigList[j-1] = bigList[j-1], bigList[j]
            continue
        if(bigList[j-1]>bigList[j]):
            bigList[j-1], bigList[j] = bigList[j],bigList[j-1]
print(bigList)