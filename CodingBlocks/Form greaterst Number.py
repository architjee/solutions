t = int(input())
for _ in range(t):
    m = int(input())
    arr =  input().split()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]+arr[i]> arr[i]+arr[j]:
                arr[j],arr[i] = arr[i], arr[j];

    print(''.join(arr))