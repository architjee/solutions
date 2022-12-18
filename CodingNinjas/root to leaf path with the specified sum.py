from os import *
from sys import *
from collections import *
from math import *

from typing import *

# Following is the structure of Tree Node
# Do not update or change the structure 


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pathSum(root: TreeNode, target: int) -> int:
    
    # Write your code
    def helper_fun(subtree, remaining_coins):
        if not subtree:
            return 0
        remaining_coins -= subtree.val
        if not subtree.left and not subtree.right and remaining_coins==0:
            return 1
        return helper_fun(subtree.left, remaining_coins) + helper_fun(subtree.right, remaining_coins)
    return helper_fun(root, target)