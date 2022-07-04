smallList = list(map(int, input().split()))
smallList.sort();
print(min(smallList[2]-smallList[1]-1, smallList[1]-smallList[0]-1))
print(max(smallList[2]-smallList[1]-1, smallList[1]-smallList[0]-1))