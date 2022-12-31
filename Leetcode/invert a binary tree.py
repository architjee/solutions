# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def aux(subtree):
            if not subtree:
                return
            subtree.left , subtree.right = subtree.right, subtree.left
            aux(subtree.left)
            aux(subtree.right)
        aux(root)
        return root