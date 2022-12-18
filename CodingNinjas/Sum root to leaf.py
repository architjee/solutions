from os import *
from sys import *
from collections import *
from math import *

# Binary tree node class for reference:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafSum(root):
    # Write your code here.
    # We need to find total sum of root to leaf paths.
    result = []
    def helper_func(subtree, previous_sum):
        if not subtree:
            return 0
        new_sum = subtree.data +( previous_sum*10)
        if not subtree.left and not subtree.right:
            result.append(new_sum)
            return new_sum
        
        left_val = helper_func(subtree.left, new_sum)
        right_val = helper_func(subtree.right, new_sum)
        
    helper_func(root,0)
    
    return sum(result)%(1000000007)
    