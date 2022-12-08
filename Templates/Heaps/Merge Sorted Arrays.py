
import heapq
def merge_sorted_arrays(sorted_arrays):
    min_heap = []

    # Build a list of iterators of each array in the sorted arrays.
    sorted_arrays_iters = [iter(x)for x in sorted_arrays]

    # Put the first element from each array into the min_heap.
    for index, it in enumerate(sorted_arrays_iters):
        firstElement = next(it, None)
        if firstElement!=None:
            heapq.heappush(min_heap, (firstElement, index))
    
    # Create a array for the result.
    result = []

    while min_heap:
        smallest_entry , smallest_array_index = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays[smallest_array_index]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element!=None:
            heapq.heappush(min_heap, (next_element, smallest_array_index))
    return result