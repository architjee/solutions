from os import *
from sys import *
from collections import *
from math import *

def findInMatrix(x, arr):

    # Write your code here
    ## We know that each column and each row is sorted.
    ## Let us begin from the Right Top most point
    row, column = 0, len(arr[0])-1
    while row<len(arr) and column>=0:
        extremity_value = arr[row][column]
        if extremity_value == x:
            return True
        elif extremity_value > x:
            column -=1
        else:
            row +=1
    return False