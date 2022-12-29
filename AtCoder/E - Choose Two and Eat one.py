n, m = map(int, input().split())
arr = list(map(int, input().split()))
import heapq
class my_max_heap:
    def __init__(self, capacity):
        self.max_heap = []
    def push(self, x):
        neg_x = -x 
        heapq.heappush(self.max_heap, neg_x)
    def exatract_max(self):
        return -1*heapq.heappop(self.max_heap)
    
    def __len__(self):
        return len(self.max_heap)
max_heap = my_max_heap(n)
for x in arr:
    max_heap.push(x)
while len(max_heap)>=2:
    first_max = max_heap.exatract_max()
    second_max = max_heap.exatract_max()
    
print(len(max_heap))
## Apparently this problem is graph question.