from os import *
from sys import *
from collections import *
from math import *
import functools
def romanToInt(s):
    mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    return functools.reduce(lambda val, index: val + (-mapping[s[index]] if mapping[s[index]]<mapping[s[index+1]] else mapping[s[index]]), reversed(range(len(s)-1)), 0)