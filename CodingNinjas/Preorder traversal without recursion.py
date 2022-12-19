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
    stack = [root]
    result = []
    while stack:
        p = stack.pop()
        if p:
            result.append(p.val)
            stack += [p.right, p.left]
    return result


