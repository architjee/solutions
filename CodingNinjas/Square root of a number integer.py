from os import *
from sys import *
from collections import *
from math import *

def sqrtN(n):

	left,right = 0, n
    while left<=right:
        mid = (left+right)//2
        mid_squared = mid*mid
        if mid_squared<=n:
            left = mid+1
        else:
            right = mid -1
    return left-1
        