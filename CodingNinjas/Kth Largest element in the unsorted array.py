from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout
import random

def kthLargest(arr, size, k):
    opg = lambda x, y: x>y
    # Write your code here.
    def partition_around_pivot(left, right, pivot_idx, opg):
        pivot_value = arr[pivot_idx]
        new_pivot_idx = left
        ## Safe keeping the pivot at rightmost index.
        arr[right], arr[pivot_idx] = arr[pivot_idx], arr[right]
        for i in range(left, right):
            if opg(arr[i], pivot_value):
                arr[i], arr[new_pivot_idx] = arr[new_pivot_idx], arr[i]
                new_pivot_idx+=1
        arr[new_pivot_idx], arr[right] = arr[right], arr[new_pivot_idx]
        return new_pivot_idx
    left, right = 0, size-1
    while left<=right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx, opg)
        if new_pivot_idx==k-1:
            return arr[new_pivot_idx]
        elif new_pivot_idx>k-1:
            right = new_pivot_idx-1
        else: # newpivotidx<k-1
            left = new_pivot_idx+1

































# Taking input using fast I/0
def takeInput():
    N,K = list(map(int, stdin.readline().strip().split(" ")))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, K, arr


tc = int(input())
while tc > 0:
    N, K, arr = takeInput()
    stdout.write(str(kthLargest(arr, N,K)) + "\n")
    tc -= 1