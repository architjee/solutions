def kthSmallLarge(arr, n, k):
    # Write your code here
    # Since we know the elements are distinct, it would be wise to sort and point out the element which is kth smallest.
    arr.sort()
    # We have inplace sorted.
    
    # We know that smallest is at 0th index, 2nd smallest is at 1st index
    smallest = arr[k-1]
    
    # We know that largest element is at n-1 index, so second largest would be at n-2
    largest  = arr[n-k]
    
    result = [smallest, largest]
    return result
