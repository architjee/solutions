size = int(input())
nums = list(map(int,input().split()))
nums = [-x for x in nums]
import heapq
heapq.heapify(nums)
x = heapq.heappop(nums)
y = heapq.heappop(nums)
z = heapq.heappop(nums)
print(-z, -y, -x) 
