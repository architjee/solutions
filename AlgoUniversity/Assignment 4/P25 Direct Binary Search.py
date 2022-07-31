def bSearch(bigList, target):
    low = 0
    high = len(bigList) -1
    while low<=high:
        mid = (low+high)//2
        if(bigList[mid]==target):
            return mid
        elif (bigList[mid]> target):
            high = mid-1
        elif (bigList[mid]< target):
            low = mid+1
    return -1


n, q = map(int,input().split())
bigList = list(map(int, input().split()))
queries = map(int, input().split())
for q in queries:
    print(bSearch(bigList, q))
