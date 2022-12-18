'''

    Following is the representation for the Binary Tree Node:

    class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
'''

def isSymmetric(root) :
    # Write your code here.
    if not root:
        return True
    def aux_symmetric_func(sub1, sub2):
        if not sub1 and not sub2:
            return True
        if not sub1 or not sub2:
            return False
        return sub1.data == sub2.data and aux_symmetric_func(sub1.left, sub2.right) and aux_symmetric_func(sub1.right, sub2.left)
    return aux_symmetric_func(root.left, root.right)