# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(pre, ino):
            if not pre or not ino:
                return None
            if len(pre)==1 and len(ino)==1:
                return TreeNode(pre[0])
            index, val=0, None
            newNode = TreeNode(pre[0])
            for index,val in enumerate(ino):
                if val == pre[0]:
                    break
            newNode.left = helper(pre[1:index+1], ino[:index+1])
            newNode.right = helper(pre[index+1:], ino[index+1:])
            return newNode
        return helper(preorder, inorder)