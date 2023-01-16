# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## Level order traversal I think is bfs question.
        if not root:
            return []
        curr_depth_nodes= [root]

        result = []
        while curr_depth_nodes:
            result.append([curr.val for curr in curr_depth_nodes])
            curr_depth_nodes = [ child for child in curr_depth_nodes for child in (child.left , child.right) if child]
        return result