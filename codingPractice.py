class ListNode:
	# Time: O(1), because assigning two fields takes constant time.
	# Pseudocode: Store the value and the reference to the next node.
	def __init__(self, value=0, next_node=None):
		self.value = value  # Save this node's data.
		self.next = next_node  # Save the link to the next node.


class TreeNode:
	# Time: O(1), because assigning three fields takes constant time.
	# Pseudocode: Store the value and the left and right child references.
	def __init__(self, value=0, left=None, right=None):
		self.value = value  # Save this node's data.
		self.left = left  # Save the left child link.
		self.right = right  # Save the right child link.


# Time: O(n) average, because each number is checked once with constant-time hash lookups.
# Pseudocode: Remember each number's index; for each number, look for its needed complement.
def two_sum(numbers, target):
	seen = {}  # Map each number already visited to its index.
	for index, number in enumerate(numbers):  # Visit each number once.
		complement = target - number  # Calculate the value needed to reach target.
		if complement in seen:  # Check whether that value appeared earlier.
			return [seen[complement], index]  # Return the two matching indices.
		seen[number] = index  # Remember this number for future iterations.
	return []  # No pair adds up to target.


# Time: O(n) average, because creating a set checks all n numbers once.
# Pseudocode: Compare the list length with the number of unique values in a set.
def contains_duplicate(numbers):
	unique_numbers = set(numbers)  # A set keeps only one copy of each value.
	return len(numbers) != len(unique_numbers)  # Different lengths mean a duplicate exists.


# Time: O(n), because both strings are scanned once; the dictionary stores character counts.
# Pseudocode: Count characters in the first string, then subtract counts using the second string.
def is_valid_anagram(first, second):
	if len(first) != len(second):  # Different lengths cannot have equal character counts.
		return False  # Stop immediately when the lengths differ.

	counts = {}  # Store how many times each character appears in first.
	for character in first:  # Count every character in the first string.
		counts[character] = counts.get(character, 0) + 1  # Increase this character's count.
	for character in second:  # Use the second string to reduce those counts.
		if character not in counts:  # This character never appeared in first.
			return False  # The strings cannot be anagrams.
		counts[character] -= 1  # Match one copy of this character.
		if counts[character] < 0:  # Second contains this character too many times.
			return False  # The strings cannot be anagrams.
	return True  # Every character matched successfully.


# Time: O(n) with O(1) extra space, because each pointer moves across the text at most once.
# Pseudocode: Move inward past punctuation, then compare lowercase characters at both pointers.
def is_valid_palindrome(text):
	left, right = 0, len(text) - 1  # Start pointers at both ends of the text.
	while left < right:  # Continue until the pointers meet.
		while left < right and not text[left].isalnum():  # Skip non-letter/digit characters on the left.
			left += 1  # Move the left pointer inward.
		while left < right and not text[right].isalnum():  # Skip non-letter/digit characters on the right.
			right -= 1  # Move the right pointer inward.
		if text[left].lower() != text[right].lower():  # Compare the meaningful characters.
			return False  # A mismatch means the text is not a palindrome.
		left += 1  # Move past the matched left character.
		right -= 1  # Move past the matched right character.
	return True  # Every pair matched.


# Time: O(n) with O(1) extra space, because each price is processed once while tracking two values.
# Pseudocode: Track the cheapest earlier price and the best profit seen so far.
def max_profit(prices):
	lowest_price = float("inf")  # Start with a price higher than any real price.
	best_profit = 0  # No transaction produces zero profit initially.
	for price in prices:  # Treat each price as a possible selling price.
		lowest_price = min(lowest_price, price)  # Keep the cheapest buying price so far.
		best_profit = max(best_profit, price - lowest_price)  # Keep the best profit so far.
	return best_profit  # Return the best possible transaction profit.


# Time: O(n) average, because each character is visited once with dictionary lookups.
# Pseudocode: Keep a sliding window and move its start past a repeated character.
def length_of_longest_substring(text):
	last_seen = {}  # Map each character to its most recent index.
	window_start = 0  # Mark the beginning of the current unique-character window.
	longest = 0  # Store the longest window length found so far.
	for index, character in enumerate(text):  # Expand the window one character at a time.
		if character in last_seen and last_seen[character] >= window_start:  # Check for a repeat inside the window.
			window_start = last_seen[character] + 1  # Move past the previous copy.
		last_seen[character] = index  # Record this character's newest position.
		longest = max(longest, index - window_start + 1)  # Update the best window length.
	return longest  # Return the longest substring without repeats.


# Time: O(log n), because each comparison cuts the sorted search range roughly in half.
# Pseudocode: Check the middle value and discard the half that cannot contain the target.
def binary_search(numbers, target):
	left, right = 0, len(numbers) - 1  # Start with the full array as the search range.
	while left <= right:  # Continue while the range still contains values.
		middle = (left + right) // 2  # Check the value halfway through the range.
		if numbers[middle] == target:  # The target was found.
			return middle  # Return its index.
		if numbers[middle] < target:  # The target must be to the right.
			left = middle + 1  # Discard the left half, including middle.
		else:  # The target must be to the left.
			right = middle - 1  # Discard the right half, including middle.
	return -1  # The target is not in the array.


# Time: O(p log m), because binary search tries O(log m) speeds and each try scans p piles.
# Pseudocode: Binary-search the smallest speed that can finish all piles within the hours.
def min_eating_speed(piles, hours):
	left, right = 1, max(piles)  # The answer must be between one and the largest pile.
	while left < right:  # Narrow the possible speed range until one value remains.
		speed = (left + right) // 2  # Test the middle eating speed.
		required_hours = sum((pile + speed - 1) // speed for pile in piles)  # Calculate hours for this speed.
		if required_hours <= hours:  # This speed is fast enough.
			right = speed  # Keep it as a possible answer and try slower speeds.
		else:  # This speed is too slow.
			left = speed + 1  # Only faster speeds can work.
	return left  # Return the smallest speed that works.


# Time: O(n) with O(n) stack space, because each bracket is pushed and popped at most once.
# Pseudocode: Push opening brackets; each closing bracket must match the latest opening bracket.
def is_valid_parentheses(text):
	pairs = {")": "(", "]": "[", "}": "{"}  # Map each closing bracket to its matching opener.
	opening = set(pairs.values())  # Store the possible opening brackets.
	stack = []  # Keep opening brackets that have not been closed yet.
	for character in text:  # Process brackets from left to right.
		if character in opening:  # Opening brackets must be matched later.
			stack.append(character)  # Put the newest opening bracket on top.
		elif not stack or stack.pop() != pairs.get(character):  # Check the matching opener.
			return False  # The bracket order is invalid.
	return not stack  # Valid input must have no unmatched opening brackets.


# Time: O(n) with O(h) call-stack space, because every tree node is visited once.
# Pseudocode: The depth is one plus the larger depth of the left and right subtrees.
def max_depth(root):
	if root is None:  # An empty subtree has depth zero.
		return 0  # Stop this recursive branch.
	left_depth = max_depth(root.left)  # Find the depth of the left subtree.
	right_depth = max_depth(root.right)  # Find the depth of the right subtree.
	return 1 + max(left_depth, right_depth)  # Count this node plus the deeper subtree.


# Time: O(n) with O(1) extra space, because each node is rewired and visited once.
# Pseudocode: Reverse each next pointer while walking forward, then return the new head.
def reverse_linked_list(head):
	previous = None  # The reversed list starts empty.
	current = head  # Begin at the original head.
	while current:  # Continue until every node has been processed.
		next_node = current.next  # Save the remaining list before changing the link.
		current.next = previous  # Point the current node backward.
		previous = current  # Move the reversed-list head forward.
		current = next_node  # Move to the next original node.
	return previous  # The last processed node is the new head.


# Time: O(n log n), because sorting dominates the single merge pass; output storage is O(n).
# Pseudocode: Sort by start, then extend the current interval or begin a new one.
def merge_intervals(intervals):
	if not intervals:  # There is nothing to merge.
		return []  # Return an empty result immediately.
	merged = []  # Store the non-overlapping intervals built so far.
	for start, end in sorted(intervals):  # Process intervals from earliest start to latest.
		if not merged or start > merged[-1][1]:  # Start a new interval if there is no overlap.
			merged.append([start, end])  # Add this interval as a separate range.
		else:  # This interval overlaps the most recent merged interval.
			merged[-1][1] = max(merged[-1][1], end)  # Extend the existing interval if needed.
	return merged  # Return all merged ranges.


# Time: O(rows * columns) with O(rows * columns) worst-case stack space, because each cell is visited once.
# Pseudocode: When land is found, use a stack to mark all connected land as visited.
def number_of_islands(grid):
	if not grid:  # An empty grid has no islands.
		return 0  # Return before trying to read its dimensions.
	rows, columns = len(grid), len(grid[0])  # Save the grid dimensions.
	islands = 0  # Count each new island discovered.

	for row in range(rows):  # Visit every row.
		for column in range(columns):  # Visit every column in this row.
			if grid[row][column] == "1":  # Unvisited land starts a new island.
				islands += 1  # Count this island once.
				stack = [(row, column)]  # Begin exploring this island from its first cell.
				grid[row][column] = "0"  # Mark the starting land as visited.
				while stack:  # Continue until all connected land is explored.
					current_row, current_column = stack.pop()  # Take one cell to explore.
					neighbors = [  # List the four cells directly next to it.
						(current_row - 1, current_column),
						(current_row + 1, current_column),
						(current_row, current_column - 1),
						(current_row, current_column + 1),
					]
					for next_row, next_column in neighbors:  # Check each neighboring cell.
						if (
							0 <= next_row < rows
							and 0 <= next_column < columns
							and grid[next_row][next_column] == "1"
						):
							grid[next_row][next_column] = "0"  # Mark valid land immediately.
							stack.append((next_row, next_column))  # Explore it later.
	return islands  # Return the number of connected land groups.


# Time: O(log steps) with O(log steps) recursion space, because fast doubling halves the input each call.
# Pseudocode: Recursively calculate Fibonacci values for half the steps, then double them with formulas.
def climbing_stairs(steps):
	# Time: O(log number) with O(log number) recursion space, because the input is halved each call.
	# Pseudocode: Find Fibonacci values for half the number, then calculate the full pair by doubling.
	def fibonacci(number):
		if number == 0:  # The base Fibonacci pair is F(0), F(1).
			return 0, 1  # Return both values needed by the formulas.

		first, second = fibonacci(number // 2)  # Recursively calculate values for half the index.
		even_result = first * (2 * second - first)  # Calculate F(2k).
		odd_result = first * first + second * second  # Calculate F(2k + 1).
		if number % 2 == 0:  # The requested index is even.
			return even_result, odd_result  # Return F(number) and F(number + 1).
		return odd_result, even_result + odd_result  # Return the odd-index pair.

	return fibonacci(steps + 1)[0]  # Ways to climb n stairs equal F(n + 1).


# Time: O(n) with O(n) extra space, because frequencies and frequency buckets each take linear space.
# Pseudocode: Count values, place them in buckets by frequency, then read buckets from highest to lowest.
def top_k_frequent(numbers, k):
	frequencies = {}  # Map each number to its occurrence count.
	for number in numbers:  # Count every input number.
		frequencies[number] = frequencies.get(number, 0) + 1  # Increase this number's count.

	buckets = [[] for _ in range(len(numbers) + 1)]  # Make one bucket for each possible frequency.
	for number, frequency in frequencies.items():  # Place each number into its frequency bucket.
		buckets[frequency].append(number)  # Group numbers with equal frequencies.

	most_frequent = []  # Store the answer in frequency order.
	for frequency in range(len(buckets) - 1, 0, -1):  # Read buckets from highest to lowest frequency.
		for number in buckets[frequency]:  # Visit each number at this frequency.
			most_frequent.append(number)  # Add it to the answer.
			if len(most_frequent) == k:  # Stop as soon as k values are collected.
				return most_frequent  # Return exactly the requested number of values.
	return most_frequent  # Return all available values if fewer than k exist.


# Time: O(n) with O(n) output space, because every linked-list node is visited once and copied to a list.
# Pseudocode: Walk through the nodes and append each value to a result list.
def linked_list_values(head):
	values = []  # Store the values in traversal order.
	while head:  # Continue until the end of the list.
		values.append(head.value)  # Copy the current node's value.
		head = head.next  # Move to the next node.
	return values  # Return all collected values.


# Time: O(1) for this fixed set of examples; generally, it is linear in the total test input size.
# Pseudocode: Call every solution with a known example and stop if any assertion is false.
def run_examples():
	assert two_sum([2, 7, 11, 15], 9) == [0, 1]  # The first two values add to 9.
	assert contains_duplicate([1, 2, 3, 1]) is True  # The value 1 appears twice.
	assert contains_duplicate([1, 2, 3, 4]) is False  # Every value is unique.
	assert is_valid_anagram("anagram", "nagaram") is True  # Both strings have the same counts.
	assert is_valid_anagram("rat", "car") is False  # The character counts differ.
	assert is_valid_palindrome("A man, a plan, a canal: Panama") is True  # Ignore case and punctuation.
	assert is_valid_palindrome("race a car") is False  # The meaningful characters do not mirror.
	assert max_profit([7, 1, 5, 3, 6, 4]) == 5  # Buy at 1 and sell at 6.
	assert length_of_longest_substring("abcabcbb") == 3  # The longest unique substring is "abc".
	assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4  # The target is at index 4.
	assert min_eating_speed([3, 6, 7, 11], 8) == 4  # Speed 4 finishes within 8 hours.
	assert is_valid_parentheses("([]{})") is True  # Every bracket closes in the correct order.
	assert is_valid_parentheses("([)]") is False  # The closing brackets are mismatched.

	tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))  # Build a tree with three levels.
	assert max_depth(tree) == 3  # Confirm the tree depth.

	head = ListNode(1, ListNode(2, ListNode(3)))  # Build a list containing 1, 2, and 3.
	assert linked_list_values(reverse_linked_list(head)) == [3, 2, 1]  # Confirm the list was reversed.
	assert merge_intervals([[1, 3], [2, 6], [8, 10], [9, 12]]) == [
		[1, 6], [8, 12]
	]  # Confirm overlapping intervals were combined.
	grid = [
		["1", "1", "0", "0", "0"],
		["1", "1", "0", "0", "0"],
		["0", "0", "1", "0", "0"],
		["0", "0", "0", "1", "1"],
	]  # Build a grid containing three separate islands.
	assert number_of_islands(grid) == 3  # Confirm the island count.
	assert climbing_stairs(5) == 8  # There are eight ways to climb five stairs.
	assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}  # Confirm the two most frequent values.


if __name__ == "__main__":
	run_examples()  # Run the examples when this file is executed directly.
	print("All examples passed.")  # Report success if no assertion failed.
