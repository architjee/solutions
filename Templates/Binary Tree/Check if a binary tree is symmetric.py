def check_symmetric(tree):
    def check_symmetric_helper(node0, node1):
        if not node0 and not node1:
            return True
        elif node0 and node1:
            return node0.data==node1.data and check_symmetric_helper(node0.left , node1.right) and check_symmetric_helper(node0.right, node1.left)
        return False #one nnode exist and other doesn't
    return not tree or check_symmetric_helper(tree.left, tree.right)