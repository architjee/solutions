## Case 1 arr = [-14,-10,2,108,108,243,285,285,285,401]
## key = 285 => 9
## key = -13 => 1
arr = [-14,-10,2,108,108,243,285,285,285,401]
import bisect
def b_search_greater(A, key):
    return bisect.bisect_right(A, key)
# print(b_search_greater(arr, -13))

def custom_b_search_greater(A, key):
    low, high = 0, len(A)-1
    ## The candidate set is A[low:high+1)
    ans = -1
    while low<=high:
        mid = (low+high)//2
        if A[mid] > key:
            ans = mid
            high=mid-1
        elif A[mid]<=key:
            low = mid+1
    return ans
print(custom_b_search_greater(arr, 285))
print(custom_b_search_greater(arr, -13))