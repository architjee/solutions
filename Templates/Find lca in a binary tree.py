import collections
def lca(tree, node0, node1):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'node'))
    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes==2:
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes==2:
            return right_result
        num_target_nodes = left_result.num_target_nodes+right_result.num_target_nodes+int(tree==node0)+int(tree==node1)
        return Status(num_target_nodes, tree if num_target_nodes==2 else None)
    return lca_helper(tree, node0, node1).node