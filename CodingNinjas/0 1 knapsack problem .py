from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    ## This is a 0 1 knapsack problem code.


def main():
    n = int(input())
    items = []
    weights = map(int, input().split())
    for w in weights:
        newItem = Item(0, w)
        items.append(newItem)
    values = map(int, input().split())

    for index, v in enumerate(values):
        items[index].value = v
    max_capacity = int(input())

    value_matrix = [[-1] * (max_capacity + 1) for item_iter in items]

    def helperFunction(item_index, available_capacity):
        if item_index < 0:
            return 0
        if value_matrix[item_index][available_capacity] == -1:
            value_without_this_item = helperFunction(item_index - 1, available_capacity)
            ## means the value doesn't exists so we will compute it.
            if items[item_index].weight > available_capacity:
                value_with_this_item=0
            else:
                value_with_this_item = items[item_index].value + helperFunction(
                    item_index - 1, available_capacity - items[item_index].weight
                )
            value_matrix[item_index][available_capacity] = max(
                value_without_this_item, value_with_this_item
            )
        return value_matrix[item_index][available_capacity]
    optimum_value = helperFunction(len(items) - 1, max_capacity) 
    return optimum_value
t = int(input())
for testcase in range(t):
    print(main())
