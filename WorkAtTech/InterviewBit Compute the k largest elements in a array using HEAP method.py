class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        ## Given A is the size of array and B is the no. of largest elements we need to extract from A.
        if not A:
            return []
        
        import heapq

        heapq.heapify(A)
        result = []
        ## Now that we have heapified the result we need not worry abouty anything, however we must create a candidate _max_ heap.
        ## Everything inside candidate_max_heap is Value, index.
        from collections import namedtuple;
        Candidate = namedtuple('Candidate', ('value', 'index'))
        candidate_max_heap = [Candidate(-A[0], 0)]
        for _ in range(B):
            candidate_idx = candidate_max_heap[0].index
            result.append(-heapq.heappop(candidate_max_heap).value)
            left_child_idx = (2 * candidate_idx) +1
            if left_child_idx<len(A):
                ## This is a valid index, we should add it to the candidate.
                heapq.heappush(candidate_max_heap, Candidate(-A[left_child_idx], left_child_idx))
            right_child_idx = (2*candidate_idx)+2 
            if right_child_idx<len(A):
                heapq.heappush(candidate_max_heap, Candidate(-A[right_child_idx], right_child_idx))


        return result