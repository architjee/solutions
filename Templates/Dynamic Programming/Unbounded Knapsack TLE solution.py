
class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        
        class Item:
            def __init__(self, value, weight):
                self.value = value
                self.weight = weight
                ## This is a unbounded knapsack problem code.
# The two arrays are N and W.
        ## Also given maximum weight capacity is wt.
        items = []
        for w in wt:
            newItem = Item(0, w)
            items.append(newItem)

        for index, v in enumerate(val):
            items[index].value = v
        max_capacity = W

        value_matrix = [[-1] * (max_capacity + 1) for item_iter in items]

        def helperFunction(item_index, available_capacity):
            if available_capacity<0:
                return 0
            if item_index < 0:
                return 0
            if value_matrix[item_index][available_capacity] == -1:
                value_without_this_item = helperFunction(item_index - 1, available_capacity)
                ## means the value doesn't exists so we will compute it.
                value_with_this_item = 0
                k=available_capacity//item_index[item_index].weight
                ## Let us say we are adding this item k times,
                ## The invariant would be that,
                while (k*items[item_index].weight) <= available_capacity :
                    value_with_k_items_of_this_type = (items[item_index].value*k) + helperFunction(item_index-1 , available_capacity - (items[item_index].weight*k))
                    value_with_this_item=max(value_with_this_item, value_with_k_items_of_this_type)
                    k+=1
                value_matrix[item_index][available_capacity] = max(value_without_this_item, value_with_this_item)
            return value_matrix[item_index][available_capacity]
        optimum_value = helperFunction(len(items) - 1, max_capacity) 
        return optimum_value

