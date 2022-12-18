# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        Result = collections.namedtuple('Result', ('num_nodes', 'ancestor'))
        def helper_fun(subtree, p, q):
            if not subtree:
                return Result(0, None)
            left_result = helper_fun(subtree.left, p, q)
            if left_result.num_nodes==2:
                return left_result
            right_result = helper_fun(subtree.right, p, q)
            if right_result.num_nodes==2:
                return right_result
            num_nodes = int(p==subtree)+int(q==subtree) + left_result.num_nodes + right_result.num_nodes
            ancestor = None
            if num_nodes==2:
                anscestor = subtree
            return Result(num_nodes, ancestor)
        return helper_fun(root, p, q).ancestor
            