from os import *
from sys import *
from collections import *
from math import *
import heapq
def Klargest(a, k, n):
    # Write your code here
    ## We are given n integers in array a.
    ## Objective is to find k largest elements in the array.
    neg_a = [-x for x in a]
    heapq.heapify(neg_a)
    result = []
    for _ in range(k):
        smallest = heapq.heappop(neg_a)
        result.append(-smallest)
    return result[::-1]
    