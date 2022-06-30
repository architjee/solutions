n = int(input())
bigList = list(map(int, input().split()));
targetSum = int(input());
bigList.sort();
for i in range(n-2):
    first = bigList[i];
    if(first >= targetSum):
        break;
    newTarget = targetSum -first;
    low = i+1;
    high = n-1;
    while low < high:
        currentSum = bigList[low]+bigList[high];
        if(currentSum == newTarget):
            print(str(first)+", "+str(bigList[low])+" and "+str(bigList[high]))
            low += 1;
            high -= 1;
        elif(currentSum > newTarget):
            high -=1;
        else:
            low += 1;
