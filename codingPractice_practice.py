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
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def max_profit(prices):
	maxProfit = 0
	minPrice = float('inf')
	for price in prices:
		minPrice = min(minPrice, price)
		maxProfit = max(maxProfit, price - minPrice)
	return maxProfit


def length_of_longest_substring(text):
	left = 0
	seen = {}
	best = 0
	for rightIndex, char in enumerate(text):
		if char in seen and seen[char] >= left:
			left = seen[char] + 1
		seen[char] = rightIndex
		best = max(best, rightIndex - left + 1)
	return best


def binary_search(numbers, target):
	left = 0
	right = len(numbers) - 1
	while left <= right:
		mid = (left + right) // 2
		if numbers[mid] == target:
			return mid
		elif numbers[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return -1
    

def min_eating_speed(piles, hours):
	pass


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
	return True


def max_depth(root):
	if not root:
		return 0
	left_depth = max_depth(root.left)
	right_depth = max_depth(root.right)
	return max(left_depth, right_depth) + 1

#Cutoff for must-know problems

def reverse_linked_list(head):
	previous = None
	current = head

	while current is not None:
		next = current.next
		current.next = previous
		previous = current
		current = next

	return previous


def merge_intervals(intervals):
	pass


def number_of_islands(grid):
	if grid is None or len(grid) == 0:
		return 0

	def dfs(grid, row, column):
		if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] == "0":
			return
		grid[row][column] = "0"
		dfs(grid, row + 1, column)
		dfs(grid, row - 1, column)
		dfs(grid, row, column + 1)
		dfs(grid, row, column - 1)

	islandCount = 0
	rows = len(grid)
	columns = len(grid[0])

	for row in range(rows):
		for column in range(columns):
			if grid[row][column] == "1":
				islandCount += 1
				dfs(grid, row, column)
	return islandCount


def climbing_stairs(steps):
	pass


def top_k_frequent(numbers, k):
	pass


def linked_list_values(head):
	values = []
	current = head
	while current:
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
	assert min_eating_speed([3, 6, 7, 11], 8) == 4

	tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	assert max_depth(tree) == 3

	head = ListNode(1, ListNode(2, ListNode(3)))
	assert linked_list_values(reverse_linked_list(head)) == [3, 2, 1]
	assert merge_intervals([[1, 3], [2, 6], [8, 10], [9, 12]]) == [
		[1, 6], [8, 12]
	]
	grid = [
		["1", "1", "0", "0", "0"],
		["1", "1", "0", "0", "0"],
		["0", "0", "1", "0", "0"],
		["0", "0", "0", "1", "1"],
	]
	assert number_of_islands(grid) == 3
	assert climbing_stairs(5) == 8
	assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}


if __name__ == "__main__":
	run_examples()
	print("All examples passed.")
