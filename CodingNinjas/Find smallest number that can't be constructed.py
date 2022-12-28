from os import *
from sys import *
from collections import *
from math import *

def findSmallestInteger(arr):
    smallest_value_not_possible = 0
    for x in sorted(arr):
        if x > smallest_value_not_possible + 1:
            break
        smallest_value_not_possible+=x
    return smallest_value_not_possible+1
    #Your code goes here.






