# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(left_subtree, right_subtree):
            if not left_subtree:
                return right_subtree, None
            if not right_subtree:
                return None, left_subtree
            left_subtree.left, left_subtree.right = helper(left_subtree.left, left_subtree.right)
            right_subtree.left, right_subtree.right = helper(right_subtree.left ,right_subtree.right)
            return right_subtree, left_subtree
        if not root:
            return None
        root.left , root.right = helper(root.left, root.right)
        return root