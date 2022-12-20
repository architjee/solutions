# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ## We need to use indices in this question as length of subarrays probably would not survive.
        indexOfInorder = { value: index for index, value in enumerate(inorder)}
        def construct_helper(in_start, in_end, post_start, post_end):
            # print('helper fn being called with ', post_start, post_end)
            if in_end<in_start or post_end<post_start:
                return None
            newNode = TreeNode(postorder[post_end])
            if in_start==in_end and post_start==post_end:
                return newNode
            in_index_of_subtree_root = indexOfInorder[postorder[post_end]]
            right_size = in_end - in_index_of_subtree_root
            newNode.left = construct_helper(in_start, in_index_of_subtree_root-1,post_start,post_end-1-right_size)
            newNode.right = construct_helper(in_index_of_subtree_root+1, in_end, post_end-right_size-1, post_end-1)
            
            return newNode
        return construct_helper(0, len(inorder)-1, 0, len(postorder)-1)