arr = [1,2,2,4,4,4,7,11,11,13]

import bisect
def v3(A, key):
    left_value = bisect.bisect_left(A,key)
    ## 3 possible scenarios.
    if left_value < len(A):
        if A[left_value]==key:
            return left_value
    return -1
key = 4

lower_limit = v3(arr, key)
print(lower_limit, bisect.bisect_right(arr, key)-1) 