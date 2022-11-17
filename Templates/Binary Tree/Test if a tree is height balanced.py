import collections
def is_height_balanced(tree):
    Status= collections.namedtuple('Status',('is_balanced', 'height'))
    def is_height_balanced_helper(tree):
        if not tree:
            return Status(True, 0)
        left_result = is_height_balanced_helper(tree.left)
        if not left_result.is_balanced:
            return left_result
        right_result = is_height_balanced_helper(tree.right)
        if not right_result.is_balanced:
            return right_result
        
        is_balanced = abs(left_result.height-right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return Status(is_balanced, height)
    return is_height_balanced_helper(tree).is_balanced