# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        height = 0
        subtree = root
        def height(subtree):
            if not subtree :
                return 0
            return max(height(subtree.left), height(subtree.right))+1
        tree_height = height(root)
        result =[-1 for x in range(tree_height)]
        import collections
        q = collections.deque()
        q.append((root, 0))
        while q:
            x, level = q.popleft()
            if not x:
                continue
            if x.left:
                q.append((x.left,level+1))
            if x.right:
                q.append((x.right, level+1))
            result[level] = x.val
        return result
