# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import * 
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        ## I think we must implement DFS.
        def dfs_extract_leaf_sequence(curr_node, result_set):
            if curr_node.left:
                dfs_extract_leaf_sequence(curr_node.left, result_set)
            if curr_node.right:
                dfs_extract_leaf_sequence(curr_node.right, result_set)
            if not curr_node.left and not curr_node.right:
                result_set.append(curr_node.val)
        left_result , right_result = [], []
        dfs_extract_leaf_sequence(root1, left_result)
        dfs_extract_leaf_sequence(root2, right_result)
        # print(left_result, right_result)
        if left_result == right_result:
            return True
        return False