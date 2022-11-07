from os import *
from sys import *
from collections import *
from math import *

def checkPalindrome(s):

    left, right = 0, len(s)-1
    while left<right:
        while not s[left].isalnum():
            left+=1
        while not s[right].isalnum():
            right-=1
        if left<right and s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True
      