def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    # we are given the stub
    subtree = tree
    while subtree:
        left_size = subtree.left.size if subtree.left else 0
        if left_size+1 < k:
            k -= left_size + 1
            subtree = subtree.right
        elif left_size+1 == k:
            return subtree
        else :
            subtree = subtree.left
    return None