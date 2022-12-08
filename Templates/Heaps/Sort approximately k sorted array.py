sequence = [1,2,3,4,5]
import itertools
import heapq
def sort_approximately_sorted_array(sequence, k):
    result = []
    min_heap = []
    ## Adds the first k elements into the min heap.
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    ## For every element, add it to min heap and extract the smallest element.
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # sequence is exhausted, iteratively extract the remainging elements.

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result

arr = list(map(int, input().split()))
print(sort_approximately_sorted_array(arr, 5))