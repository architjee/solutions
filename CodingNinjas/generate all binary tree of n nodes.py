from os import *
from sys import *
from collections import *
from math import *

# Following is the BinaryTreeNode Class Structure

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findAllTrees(n):
    # Write your code here.
    if n==0:
        return []
    if n==1:
        return [BinaryTreeNode(0)]
    def getTree(left_subtree, right_subtree):
        new_tree = BinaryTreeNode(0)
        new_tree.left = left_subtree
        new_tree.right = right_subtree
        return new_tree
    result = []
    for left_subsize in range(n):
        right_subsize = n-1-left_subsize
        left_subrees = findAllTrees(left_subsize)
        right_subtrees = findAllTrees(right_subsize)
        result += [getTree(left, right) for left in left_subrees for right in right_subtrees]
    return result