from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def combinations(n :int,k :int) -> List[List[int]]:
    result = []
    # Write your code here.
    def directed_combination(offset, partial_combination):
        if len(partial_combination)==k:
            result.append(list(partial_combination))
            return
        ## Generate remaining combinations over [offset, n-1] of size nums_remaining.
        nums_remaining = k - len(partial_combination)
        