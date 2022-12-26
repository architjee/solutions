import heapq
n = int(input())
min_heap = []
for _ in range(n):
    query = list(map(int, input().split()))
    if query[0]==1:
        heapq.heappush(min_heap, query[1])
    elif query[0]==2:
        print(heapq.heappop(min_heap))