low = 0;
n= int(input());
bigList = []
for i in range(n):
    bigList.append(int(input()));
bigList.sort()
high = n-1;
targetSum = int(input());
while low<=high:
    currentSum = bigList[low]+bigList[high]
    if(currentSum == targetSum):
        print(bigList[low], "and", bigList[high]);
        low+=1;
        high-=1;
    elif(currentSum<targetSum):
        low +=1;
    else:
        high -=1;