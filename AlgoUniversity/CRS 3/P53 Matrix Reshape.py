n,m,r,c = map(int, input().split())
bigList = []
def print2DArray(arr):
    for x in arr:
        for items in x:
            print(items, end=' ')
        print()
if n*m == r*c:
    for _ in range(n):
        row = list(map(int, input().split()))
        bigList.extend(row)
    reshapedArray = []

    # print("Reshaping is possible")
    i=0
    for rows in range(r):
        tempArray = []
        for cols in range(c):
            tempArray.append(bigList[i])
            i+=1
        reshapedArray.append(tempArray)
    print2DArray(reshapedArray)
else:
    for _ in range(n):
        print(input())
