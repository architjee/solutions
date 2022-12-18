# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def aux_symmetric_func(sub1, sub2):
            if not sub1 and not sub2:
                return True
            if not sub1 or not sub2:
                return False
            return sub1.val == sub2.val and aux_symmetric_func(sub1.left, sub2.right) and aux_symmetric_func(sub1.right, sub2.left)
        return aux_symmetric_func(root.left, root.right)