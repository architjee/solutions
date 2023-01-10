# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def aux(subtree1, subtree2):
            if not subtree1 and not subtree2:
                return True
            if not subtree1 or not subtree2:
                return False
            return subtree1.val==subtree2.val and aux(subtree1.left, subtree2.left) and aux(subtree1.right, subtree2.right)
        return aux(p, q)