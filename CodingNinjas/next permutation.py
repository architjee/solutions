from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    i=n
    for i in reversed(range(n)):
        if i==0:
            permutation.sort()
            return permutation
        elif permutation[i-1]<permutation[i]:
            break
    e = i -1
    j=i+1
    for j in reversed(range(e+1, n)):
        if permutation[j]>permutation[e]:
            break
    permutation[e], permutation[j] = permutation[j], permutation[e]
    def reverse(start_idx, end_idx):
        while start_idx<end_idx:
            permutation[start_idx], permutation[end_idx] = permutation[end_idx], permutation[start_idx]
            start_idx+=1
            end_idx-=1
    reverse(e+1, n-1)
    return permutation