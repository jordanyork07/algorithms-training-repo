"""Additional pattern-practice file for the next 2 days of interview prep.

Focus areas:
- sliding window
- stack
- linked list
- dfs/bfs
- heap / top-k
- intervals

Each function is intentionally left as a stub so you can practice solving them in
one place and run the built-in self-tests as you go.
"""


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# ---------------------------------------------------------------------------
# 1. Sliding Window
# ---------------------------------------------------------------------------

def longest_substring_without_repeating_chars(s):
    """Return the length of the longest substring without repeating characters."""
    left = 0
    seen = {}
    best = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        best = max(best, right - left + 1)

    return best

# A second sliding-window-style practice question:
# Given a list of ints and a window size k, return the maximum sum of any subarray of size k.
def max_sum_subarray_of_size_k(nums, k):
    start = 0
    current_sum = 0
    max_sum = float('-inf')
    for end in range(len(nums)):
        current_sum += nums[end]
        if end - start + 1 == k:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[start]
            start += 1
    return max_sum


# ---------------------------------------------------------------------------
# 2. Stack
# ---------------------------------------------------------------------------

def valid_parentheses(s):
    """Return True if the brackets are balanced."""
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack


# ---------------------------------------------------------------------------
# 3. Linked Lists
# ---------------------------------------------------------------------------

def reverse_linked_list(head):
    """Reverse a singly linked list and return the new head."""
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


# ---------------------------------------------------------------------------
# 4. DFS / BFS
# ---------------------------------------------------------------------------

def number_of_islands(grid):
    """Count the number of connected land components in a binary grid."""

    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    if grid is None or len(grid) == 0:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
                


# ---------------------------------------------------------------------------
# 5. Heap / Top-K
# ---------------------------------------------------------------------------

def top_k_frequent(nums, k):
    """Return the k most frequent elements."""
    raise NotImplementedError("Implement this function.")


# ---------------------------------------------------------------------------
# 6. Intervals
# ---------------------------------------------------------------------------

def merge_intervals(intervals):
    """Merge overlapping intervals and return the merged list."""
    raise NotImplementedError("Implement this function.")


# ---------------------------------------------------------------------------
# Helper functions for testing
# ---------------------------------------------------------------------------

def linked_list_from_values(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def linked_list_to_values(head):
    values = []
    while head is not None:
        values.append(head.value)
        head = head.next
    return values


def tree_from_list(values):
    if not values:
        return None

    def build(index):
        if index >= len(values) or values[index] is None:
            return None
        return TreeNode(values[index], build(index * 2 + 1), build(index * 2 + 2))

    return build(0)


# ---------------------------------------------------------------------------
# Self-tests for the targeted patterns
# ---------------------------------------------------------------------------

def run_self_tests():
    # Sliding window
    assert longest_substring_without_repeating_chars("abcabcbb") == 3
    assert longest_substring_without_repeating_chars("bbbbb") == 1
    assert longest_substring_without_repeating_chars("pwwkew") == 3
    assert max_sum_subarray_of_size_k([1, 3, 2, 6, 4, 5], 3) == 15

    # Stack
    assert valid_parentheses("()[]{}") is True
    assert valid_parentheses("([)]") is False
    assert valid_parentheses("") is True

    # Linked list
    head = linked_list_from_values([1, 2, 3, 4])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_values(reversed_head) == [4, 3, 2, 1]

    # DFS/BFS
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert number_of_islands(grid) == 3

    # Heap / top-k
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert top_k_frequent([1], 1) == [1]

    # Intervals
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [9, 12]]) == [[1, 6], [8, 12]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]

    print("All pattern-practice tests passed.")


if __name__ == "__main__":
    run_self_tests()
