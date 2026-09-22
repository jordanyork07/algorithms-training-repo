"""Two additional mock interview questions with practice test cases.

Implement each function, then run:
    python3 interview-simulation/mock_questions_extra.py
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 1. Product of Array Except Self
# Given an array of integers, return an array where each position contains
# the product of every number except the number at that position.
# Do not use division.
# Example: [1, 2, 3, 4] -> [24, 12, 8, 6]

def product_except_self(nums):
    length = len(nums)
    answer = [1] * length

    left_product = 1
    for i in range(length):
        answer[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

# 2. Binary Tree Level Order Traversal
# Return the values of a binary tree grouped by depth from left to right.
# Example: [3, 9, 20, None, None, 15, 7] -> [[3], [9, 20], [15, 7]]

def level_order(root):
    if not root:
        return []

    result = []
    queue = [root]
    while queue:
        level_size = len(queue)
        level_values = []
        for _ in range(level_size):
            node = queue.pop(0)
            level_values.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_values)
    return result


def tree_from_list(values):
    if not values:
        return None

    def build(index):
        if index >= len(values) or values[index] is None:
            return None
        return TreeNode(values[index], build(index * 2 + 1), build(index * 2 + 2))

    return build(0)


def run_self_tests():
    # Product of Array Except Self
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([5]) == [1]

    # Binary Tree Level Order Traversal
    root = tree_from_list([3, 9, 20, None, None, 15, 7])
    assert level_order(root) == [[3], [9, 20], [15, 7]]
    assert level_order(tree_from_list([1])) == [[1]]
    assert level_order(None) == []

    print("All extra mock question tests passed.")


if __name__ == "__main__":
    run_self_tests()