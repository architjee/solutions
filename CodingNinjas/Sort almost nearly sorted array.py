from os import *
from sys import *
from collections import *
from math import *
import itertools
import heapq
def nearlySorted(arr, k):
    # Write your code here
    # We are given array arr of n elements,
    # each element is at most k away from ites target position.
    min_heap = []
    result = []
    for x in itertools.islice(arr, k):
        heapq.heappush(min_heap, x)

    for x in itertools.islice(arr, k, len(arr)):
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result