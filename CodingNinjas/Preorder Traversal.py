from os import *
from sys import *
from collections import *
from math import *

# Following is the structure of Tree Node
# Do not update or change the structure 

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorderTraversal(root):
    # Write your code here
    # Return a list 
    ## This is the basic recursive implementation of preorder traversal.
    result = []
    def helper(subtree):
        if not subtree:
            return 
        result.append(subtree.val)
        helper(subtree.left)
        helper(subtree.right)
    helper(root)
    return result


