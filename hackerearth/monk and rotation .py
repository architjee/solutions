t = int(input())
for ti in range(t):
    n, k = map(int,input().split())
    k = k%n
    array = list(map(int, input().split()))
    def reverse(start_idx, end_idx):
        while start_idx<end_idx:
            array[start_idx], array[end_idx] = array[end_idx], array[start_idx]
            start_idx+=1
            end_idx-=1
    reverse(0, n-k-1)
    reverse(n-k, n-1)
    reverse(0, n-1)
    print(*array, sep=' ')