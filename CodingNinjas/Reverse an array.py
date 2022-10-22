from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    # Write your code here.
    # THey are considering 0 based indexing. So we must reverse the array after m
    def reverseArrayUtil(arr, i, j):
        while i<j:
            arr[i], arr[j]=arr[j], arr[i]
            i+=1
            j-=1
    reverseArrayUtil(arr, m+1, len(arr)-1)
    return arr
