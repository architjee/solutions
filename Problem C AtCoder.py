def rotate(temp, x):
    if(x == 0):
        return temp
    arr = temp[-x:]+temp[:len(temp)-x]
    return arr
n, Q= map(int, input().split());
arr =list(input())
storeRotations = 0;
for q in range(Q):
    t, x = map(int, input().split());
    if(t==1):
        storeRotations += x
    else:
        arr = rotate(arr, storeRotations%len(arr))
        print(arr[x-1])
        storeRotations = 0
