import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        ## Always add the incoming element to the min_heap.
        heapq.heappush(self.min_heap, num)
        ## Extract the smallest from min_heap
        smallest = heapq.heappop(self.min_heap)
        heapq.heappush(self.max_heap, -smallest)

        ## Below condition checks if 'Oops we added extra in max_heap, lets push it to min_heap'
        if len(self.max_heap)>len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    def findMedian(self) -> float:
        if len(self.min_heap)==len(self.max_heap):
            return (self.min_heap[0]-self.max_heap[0])/2
        else:
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()