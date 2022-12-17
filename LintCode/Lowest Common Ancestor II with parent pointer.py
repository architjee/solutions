"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        if not A:
            return B
        if not B:
            return A
        # write your code here
        height1 = 0
        runner = A
        while runner!=None:
            runner = runner.parent
            height1+=1
        runner = B
        height2 = 0
        while runner!=None:
            runner = runner.parent
            height2 += 1
        # Now the difference in height will decide which node should travel more.
        if height1>height2:
            A,B = B, A
            height1, height2 = height2, height1
        # Travel the distance diff height in height 2
        runner2 = B
        for k in range(height2-height1):
            runner2= runner2.parent
        
        while A.val!=runner2.val and A.parent and runner2.parent:
            A=A.parent
            runner2 = runner2.parent
        return A
