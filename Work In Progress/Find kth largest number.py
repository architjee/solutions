import random
k=5
A = [-10,-20,-30,40,3,50,23]
def find_kth(comp):
    def partition_around_pivot(left, right, pivot_idx):
        pivot_value = A[pivot_idx]
        ## We should safekeep the pivot_idx value
        new_pivot_idx = left
        A[pivot_idx], A[right] = A[right], A[pivot_idx]
        for i in range(left, right):
            if comp(A[i], pivot_value):
                A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                new_pivot_idx+=1
        A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
        return new_pivot_idx
    left, right = 0, len(A)-1
    while left<=right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
        if new_pivot_idx == k-1:
            return A[new_pivot_idx]
        elif new_pivot_idx>k-1:
            right = new_pivot_idx-1
        else:
            left = new_pivot_idx+1
opg = lambda x, y: x>y
print(find_kth(opg))