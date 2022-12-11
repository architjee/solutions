## This is the classical knapsack problem.


def max_value_subject_to_capacity(items, capacity):
    ## Since capacity is included in the possible weight options==> we will create array with size capcity+1 to include it.
    value_arr = [[-1] * (capacity+1) for i in items]

    def helper_function(item_left, available_capacity):
        ## Altho we can never let the weight be less than zero. But no. of items used in the knapsack could be item_i,
        if item_left<0:
            return 0
            ## Because no more items are left to consider, we have exhausted all posibilities.
        if value_arr[item_left][available_capacity]==-1:
            val_without_this_item = helper_function(item_left-1, available_capacity)
            if available_capacity<items[item_left].weight:
                val_with_this_item = 0
            else:
                ## It is possible to include this item, therefore.
                val_with_this_item = items[item_left].value + helper_function(item_left-1, available_capacity-items[item_left].weight)
            value_arr[item_left][available_capacity] = max(val_without_this_item, val_with_this_item)
        return value_arr[item_left][available_capacity]
    
    return helper_function(len(items)-1, capacity)

## Now we should test this function .

class Item:
    def __init__(self, value=0, weight=0):
        self.value = value
        self.weight = weight
items = []
values = [1,2,3]
weights = [4,5,6]
capacity = 3
## Output should be zero.


values = [1,2,3]
weights = [4,5,1]
capacity = 4
## output should be 1





values = [10,15,40]
weights = [1,2,3]
capacity = 6
## output should be 1
for x in range(len(values)):
    i = Item(values[x], weights[x])
    items.append(i)
print(max_value_subject_to_capacity(items, capacity))