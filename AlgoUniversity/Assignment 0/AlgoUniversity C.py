
smallList = list(map(int, input().split()))
smallList.sort();
maxMoves = 0
if(smallList[0]+1==smallList[1] and smallList[1]+1==smallList[2]):
    # They are already consecutive.
    minNo = 0;
    maxNo = 0;
elif(smallList[0]+1==smallList[1]):
    if(smallList[1]+2==smallList[2]):
        minNo = 1
        maxMoves = 1
    else:
        minNo = 2 
elif  smallList[1]+1==smallList[2]:
    if(smallList[0]+2==smallList[1]):
        minNo = 1
        maxMoves = 1
    else:
        minNo = 2
else:
    minNo = min(2, smallList[2]-smallList[1]-1, smallList[1]-smallList[0]-1)
print(minNo)
print(max(maxMoves, smallList[2]-smallList[1]-1, smallList[1]-smallList[0]-1))