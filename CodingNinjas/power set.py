from os import *
from sys import *
from collections import *
from math import *

def pwset(v):
    # Write your code here
    # Return a 2-D list containing all subsets
    ans = []
    def pow_set_helper(idx,partial):
        if idx==len(v):
            ans.append(partial[:])
            return
        
        # We can include element at idx
        partial.append(v[idx])
        pow_set_helper(idx+1, partial)
        partial.pop()
        # Choose to not include it in the power set
        pow_set_helper(idx+1, partial)
    pow_set_helper(0,[])
    ans.sort()
    return ans
        