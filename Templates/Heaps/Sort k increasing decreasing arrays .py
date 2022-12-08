def sort_k_increasing_decreasing_array(A):
    # Create two constants 
    INCREASING , DECREASING = range(2)
    start_idx = 0
    subarray_type = INCREASING
    sorted_subarrays=[]
    for i in range(1, len(A)+1):
        # We have reached the end of array or, 
        if i==len(A) or (A[i-1]>=A[i] and INCREASING) or (A[i-1]<A[i] and DECREASING):
            if subarray_type==INCREASING:
                sorted_subarrays.append(A[start_idx:i])
                subarray_type = DECREASING
            else:
                sorted_subarrays.append(A[i-1:start_idx-1:-1])
                subarray_type = DECREASING
        start_idx = i

    print(sorted_subarrays)
    

