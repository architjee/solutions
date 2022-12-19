

def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    if node.right:
        ## That means left most in node.right
        subtree = node.right
        while subtree.left:
            subtree = subtree.left
        return subtree
    while node.parent and node.parent.right is node:
        node = node.parent
    return node.parent
