from os import *
from sys import *
from collections import *
from math import *

def maximumValue(items, n, w):
    # ITEMS contains [weight, value] pairs.
    for i in range(len(items)):
        ## Adding a 3rd index to the pair, i.e. value per weight ratio
        items[i]+=[items[i][1]/items[i][0]]
    items.sort(key=lambda x: x[2], reverse=True)
    i=0
    total_value = 0
    while w>0 and i<len(items):
        if w >= items[i][0]:
            total_value += items[i][2]*1
            w-=items[i][0]
        else:
            ## Weight is less, we can take fractional part of it.
            total_value += items[i][2]*w
            w-=w
        i+=1
    return total_value