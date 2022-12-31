from os import *
from sys import *
from collections import *
from math import *

## Ops
def main(n, weights, prices, max_capacity):
    # print('prices and weights is ',weights, prices)
    matrix = [[0]*(max_capacity+1) for x in range(1)]
    for i in range(n):
        for avail_capacity in reversed(range(max_capacity+1)):
            without_this_item = matrix[i%1-1][avail_capacity]
            with_this_item = (prices[i-1]+ matrix[i%1-1][avail_capacity-weights[i-1]]) if avail_capacity>=weights[i-1] else 0
            matrix[i%1][avail_capacity]= max(without_this_item, with_this_item)
    print(matrix[-1][-1])


## Read input as specified in the question.
t = int(input())
for t_it in range(t):
    n = int(input())
    weights = list(map(int,input().split()))
    prices = list(map(int, input().split()))
    max_capacity = int(input())
    main(n, weights, prices, max_capacity)

## Print output as specified in the question.
