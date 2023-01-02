from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    d= {}
    def mox(idx, k):
        if k<0 or idx<0:
            return False
        key = (idx, k)
        if key not in d:
            if k==0:
                d[key] = True
                return d[key]
            if any([mox(idx-1, k), mox(idx-1,k-arr[idx])]):
                d[key] = True
                return d[key]
            d[key] = False
        return d[key]
    return mox(len(arr)-1, k)
    
    

