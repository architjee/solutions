def sortTheArrayAroundPivot(pivot_index, A):
    
    pivot = A[pivot_index]

    # We must maintain 3 invariants.
    # A[:smaller]-> less than pivot elements
    # A[smaller:equal]-> equal to pivot elements
    # A[equal:larger]-> unclassified elements
    # A[larger:] -> Elements greater than pivot
    
    smaller, equal, larger = 0, 0, len(A)
    while equal<larger:
        element = A[equal]
        if element<pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            equal+=1
            smaller+=1
        elif element==pivot:
            equal+=1
        else:
            larger-=1
            A[larger], A[equal] = A[equal], A[larger]
