class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def two_sum(numbers, target):
    pass


def contains_duplicate(numbers):
    pass


def is_valid_anagram(first, second):
    pass


def is_valid_palindrome(text):
    pass


def max_profit(prices):
    pass


def length_of_longest_substring(text):
    pass


def binary_search(numbers, target):
    pass


def is_valid_parentheses(text):
    pass


def max_depth(root):
    pass


# Cutoff for must-know problems

def reverse_linked_list(head):
    pass


def number_of_islands(grid):
    pass


def linked_list_values(head):
    pass


# These tests are intentionally unchanged so you can implement one function at a time.
def run_examples():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert length_of_longest_substring("abcabcbb") == 3
    assert is_valid_anagram("anagram", "nagaram") is True
    assert is_valid_anagram("rat", "car") is False
    assert is_valid_palindrome("A man, a plan, a canal: Panama") is True
    assert is_valid_palindrome("race a car") is False
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert is_valid_parentheses("([]{})") is True
    assert is_valid_parentheses("([)]") is False

    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(tree) == 3

    head = ListNode(1, ListNode(2, ListNode(3)))
    assert linked_list_values(reverse_linked_list(head)) == [3, 2, 1]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert number_of_islands(grid) == 3


if __name__ == "__main__":
    run_examples()
    print("All examples passed.")
