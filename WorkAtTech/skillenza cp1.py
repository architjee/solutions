size = int(input())
nums = list(map(int,input().split()))
def custom_selection_sort(array):
    ## Find the minimum in range 
    def find_min_between_indexes(start, end):
        min_element_index = start
        while start<=end:
            if array[start]<array[min_element_index]:
                min_element_index = start
            start+=1
        return min_element_index
    for indices in range(len(nums)):
        min_i = find_min_between_indexes(indices, len(nums)-1)
        array[indices], array[min_i]= array[min_i], array[indices]
custom_selection_sort(nums)
print(nums)