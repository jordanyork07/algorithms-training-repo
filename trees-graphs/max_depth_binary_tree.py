"""
Given the root of a binary tree, return its maximum depth.

The depth of a tree is the number of nodes along the longest path from the root
node down to the farthest leaf.

Constraints:
- 0 <= number of nodes <= 10^5
- Node values are arbitrary integers.

Example:
root = [3, 9, 20, None, None, 15, 7]
return 3

How to test this:
pytest -q reference_tests -k max_depth_binary_tree
# or
pytest -q reference_tests/test_reference_solutions.py -k max_depth_binary_tree
"""


def max_depth_binary_tree(root):
    if root is None:
        return 0
    return 1 + max(max_depth_binary_tree(root.left), max_depth_binary_tree(root.right))
    
