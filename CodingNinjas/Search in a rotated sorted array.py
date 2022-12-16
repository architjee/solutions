def search(arr, target) :
    # Write your code here.
    ## We are give the code stub,
    # arr and target are given to us.
    mid = 0
    left, right = 0, len(arr)-1
    while left<right:
        mid = (left+right)//2
        if arr[mid]>arr[right]:
            left = mid + 1
        else:
            right = mid
        
    ## mid is our minimum point
    # Now we will perform two binary search 1. [0, mid-1] and [mid , len(arr)-1]
    def custom_bserch(start_idx, end_idx, search_key):
        low, high = start_idx, end_idx
        while low<=high:
            mid =(low+high)//2
            if arr[mid]==search_key:
                return mid
            elif arr[mid]>search_key:
                high = mid-1
            else:
                low = mid+1
        return -1
    
    if not left:
        return custom_bserch(0, len(arr)-1, target)
    ans_partition_1 = custom_bserch(0, left-1, target)
    ans_partition_2 = custom_bserch(left, len(arr)-1, target)
    if ans_partition_1==-1:
        return ans_partition_2
    if ans_partition_2==-1:
        return ans_partition_1
    return -1
    