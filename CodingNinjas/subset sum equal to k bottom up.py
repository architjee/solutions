from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    matrix = [[False for x in range(k+1)] for _ in range(n)]
    for partial_sum in range(k+1):
        for idx in range(n):
            if partial_sum == 0:
                matrix[idx][partial_sum]=True
                continue
            if idx == 0 :  ## And partial_sum is not zero.
                matrix[idx][partial_sum]= matrix[idx][partial_sum] if arr[idx]>=partial_sum else False
                if arr[idx]==partial_sum:
                    matrix[idx][partial_sum]=True
                continue
            matrix[idx][partial_sum] = matrix[idx-1][partial_sum]
            if partial_sum>=arr[idx]:
                matrix[idx][partial_sum] = matrix[idx-1][partial_sum] or matrix[idx-1][partial_sum-arr[idx]]
    return matrix[-1][-1]
    

