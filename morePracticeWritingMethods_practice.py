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
    seen = {}

    for i, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return [seen[complement], i]
        seen[number] = i

    return []


def contains_duplicate(numbers):
    return len(numbers) != len(set(numbers))


def is_valid_anagram(first, second):
    return sorted(first) == sorted(second)


def is_valid_palindrome(text):
    cleanedString = ''.join(char.lower() for char in text if char.isalnum())
    return cleanedString == cleanedString[::-1]


def max_profit(prices):
    minProf = float('inf')
    maxProf = float('-inf')

    for p in prices:
        minProf = min(minProf, p)
        maxProf = max(maxProf, p - minProf)

    return maxProf


def length_of_longest_substring(text):
    left = 0
    seen = {}
    best = 0

    for right, char in enumerate(text):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        best = max(best, right - left + 1)

    return best


def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def is_valid_parentheses(text):
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in text:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return not stack


def max_depth(root):
    if not root:
        return 0
    leftDepth = max_depth(root.left)
    rightDepth = max_depth(root.right)

    return 1 + max(leftDepth, rightDepth)


# Cutoff for must-know problems

def reverse_linked_list(head):
    previous = None
    current = head

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def number_of_islands(grid):
    if not grid or len(grid) == 0:
        return 0

    islandCount = 0
    totalRows = len(grid)
    totalColumns = len(grid[0])

    def dfs(row, column):
        if 0 > row or row >= totalRows or 0 > column or column >= totalColumns or grid[row][column] == "0":
            return
        grid[row][column] = "0"
        dfs(row - 1, column)
        dfs(row + 1, column)
        dfs(row, column - 1)
        dfs(row, column + 1)

    for row in range(totalRows):
        for column in range(totalColumns):
            if grid[row][column] == "1":
                islandCount += 1
                dfs(row, column)

    return islandCount

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        lastMerged = merged[-1]
        if current[0] <= lastMerged[1]:
            lastMerged[1] = max(lastMerged[1], current[1])
        else:
            merged.append(current)

    return merged

def linked_list_values(head):
    values = []
    current = head

    while current is not None:
        values.append(current.value)
        current = current.next

    return values


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

    assert merge_intervals([[1, 3], [2, 6], [8, 10], [9, 12]]) == [
		[1, 6], [8, 12]
	]

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
