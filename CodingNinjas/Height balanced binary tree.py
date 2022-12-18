from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

import collections
def isBalancedBT(root):
    
    # Write your code here
    # Return True/False
    Result = collections.namedtuple('Result', ('is_balanced', 'height'))
    def helperFunc(node):
#         print('call stack logs', 'helper func', node)
        if not node:
            return Result(True, 0)
        left_result = helperFunc(node.left)
        if not left_result.is_balanced:
            return left_result
        right_result = helperFunc(node.right)
        if not right_result.is_balanced:
            return right_result
        is_balanced = abs(left_result.height-right_result.height)<=1
        height =max( left_result.height, right_result.height)+1
        return Result(is_balanced, height)
    return helperFunc(root).is_balanced
