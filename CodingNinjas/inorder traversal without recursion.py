from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''


def getInOrderTraversal(root):
    
    # Write your code here.
    stack = []
    result = []
    subtree = root
    while stack or subtree:
        if subtree:
            stack.append(subtree)
            subtree = subtree.left
        else:
            subtree = stack.pop()
            result.append(subtree.data)
            subtree= subtree.right
    return result
