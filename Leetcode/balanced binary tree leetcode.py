# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import *
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
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
