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
    result = []
    
    ## Inorder Traversal is like left child first then the node itself and then finally the right child.
    def helper(subtree):
        if not subtree:
            return
        helper(subtree.left)
        result.append(subtree.data)
        helper(subtree.right)
    helper(root)
    return result
