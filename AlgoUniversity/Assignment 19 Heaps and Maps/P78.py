import heapq
n =int(input())
length_inp = list(map(int,input().split()))
min_heap = length_inp
heapq.heapify(min_heap)
cost = 0
while len(min_heap)>1:
    min_val1 = heapq.heappop(min_heap)
    min_val2 = heapq.heappop(min_heap)
    new_length = min_val1 + min_val2
    cost += new_length
    heapq.heappush(min_heap, new_length)
print(cost)