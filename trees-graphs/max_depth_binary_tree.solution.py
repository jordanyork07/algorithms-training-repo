"""Reference solution for max_depth_binary_tree."""


def max_depth_binary_tree(root):
    if root is None:
        return 0
    return 1 + max(max_depth_binary_tree(root.left), max_depth_binary_tree(root.right))
