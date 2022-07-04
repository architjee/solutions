n = int(input())
bigList = []
for i in range(n):
    bigList.append(int(input()))
target = int(input())
low = 0;
high = n - 1;
result = -1;
while low<=high:
    mid = (low+high)//2;
    if(bigList[mid]==target):
        result = mid;
        break;
    elif(bigList[mid]<target):
        low = mid +1;
    else:
        high = mid-1;
print(result)