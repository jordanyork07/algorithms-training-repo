"""Practice file for the interview-simulation mock questions.

Use this file to implement and test the listed interview problems in one place.
Run it with:
    python interview-simulation/mock_questions_practice.py
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Longest substring without repeating characters
# Example: "abcabcbb" -> 3

def longest_substring_without_repeating_chars(s):
    left = 0
    seen = {}
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best


# 2. Given a sorted array, find a pair that sums to a target.
# Example: [1, 2, 3, 4, 6], 6 -> [1, 3]

def pair_with_target_sum(nums, target):
    for num in num:
        complement = target - num
        if complement in nums:
            return [nums.index(num), nums.index(complement)]
    return []


# 3. Determine if a string is a valid palindrome after removing at most one character.
# Example: "aba" -> True, "abca" -> True, "abc" -> False

def valid_palindrome_after_removing_one_char(s):
    def is_palindrome_range(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1
    return True


# 4. Merge overlapping intervals.
# Example: [[1, 3], [2, 6], [8, 10], [15, 18]] -> [[1, 6], [8, 10], [15, 18]]

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)

    return merged


# 5. Count the number of islands in a grid.
# Example: [[1,1,0],[1,0,1],[0,0,1]] -> 2

def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    def dfs(r, c):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and not visited[r][c]:
            visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count


# 6. Find the minimum number of coins needed to reach a target.
# Example: coins=[1, 3, 4], target=6 -> 2 (3 + 3)

def min_coins_to_target(coins, target):
    raise NotImplementedError("Implement this function.")


# 7. Search for a value in a sorted matrix.
# Example: [[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9 -> True

def search_sorted_matrix(matrix, target):
    for row in matrix:
        if target in row:
            return True
    return False


# 8. Determine whether you can reach the last index by jumping.
# Example: [2, 3, 1, 1, 4] -> True

def can_jump(nums):
    max_reachable = 0
    for i, jump in enumerate(nums):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + jump)
    return True


# 9. Count the number of ways to climb a staircase.
# Example: n=5 -> 8

def climb_stairs(n):
    if n <= 1:
        return 1
    first, second = 1, 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


# 10. Given a binary tree, compute its maximum depth.
# Example: root = [3,9,20,None,None,15,7] -> 3

def max_depth_binary_tree(root):
    if root is None:
        return 0
    leftDepth = max_depth_binary_tree(root.left)
    rightDepth = max_depth_binary_tree(root.right)
    return max(leftDepth, rightDepth) + 1


# --- Optional helper for tree tests ---

def tree_from_list(values):
    if not values:
        return None

    def build(index):
        if index >= len(values) or values[index] is None:
            return None
        return TreeNode(values[index], build(index * 2 + 1), build(index * 2 + 2))

    return build(0)


# --- Self-test harness ---
# Replace the assertions with your own implementations as you work.

def run_self_tests():
    assert longest_substring_without_repeating_chars("abcabcbb") == 3
    assert longest_substring_without_repeating_chars("bbbbb") == 1
    assert longest_substring_without_repeating_chars("pwwkew") == 3

    assert pair_with_target_sum([1, 2, 3, 4, 6], 6) == [1, 3]
    assert pair_with_target_sum([2, 3, 4], 6) == [0, 2]
    assert pair_with_target_sum([1, 2, 3], 9) == []

    assert valid_palindrome_after_removing_one_char("aba") is True
    assert valid_palindrome_after_removing_one_char("abca") is True
    assert valid_palindrome_after_removing_one_char("abc") is False

    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]

    assert count_islands([
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]) == 3

    assert min_coins_to_target([1, 3, 4], 6) == 2
    assert min_coins_to_target([2], 3) == -1

    assert search_sorted_matrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9) is True
    assert search_sorted_matrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 10) is False

    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False

    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(5) == 8

    root = tree_from_list([3, 9, 20, None, None, 15, 7])
    assert max_depth_binary_tree(root) == 3
    assert max_depth_binary_tree(None) == 0

    print("All mock question tests passed.")


if __name__ == "__main__":
    run_self_tests()
