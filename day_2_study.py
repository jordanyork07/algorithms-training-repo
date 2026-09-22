"""Day 2 interview preparation worksheet.

Day 2 schedule:
- 0-20 min: Two Sum, then Binary Search from scratch.
- 20-60 min: Mock interview #1, Longest Substring Without Repeating Characters.
- 60-100 min: Mock interview #2, Number of Islands.
- 100-120 min: Complexity, Python tools, and pattern cheat sheet review.

Study rules:
- Use a 40-minute timer for each mock interview.
- Speak through clarification, brute force, pattern, code, tests, and complexity.
- Do not look at a solution until the timer ends.
- Run the tests below after completing each method.

Prompts to say out loud:
- Sliding window: "I expand right, then move left until the window is valid."
- Number of Islands: "I mark each visited land cell so it is not processed again."
- Complexity: explain why the final time and space costs are what they are.

Pattern review:
Hash Map / Set -> lookup, frequency, duplicates
Two Pointers -> sorted arrays, palindrome, pairs
Sliding Window -> contiguous substring or subarray
Binary Search -> sorted or monotonic search space
Stack -> matching, nesting, most recent item
DFS/BFS -> trees, grids, connected things

Use this interview sequence for every problem:
Clarify -> Example -> Brute force -> Pattern -> Optimal approach -> Code -> Test -> Complexity

Run the included checks with:
    python day_2_study.py

The methods intentionally start unfinished. Replace each NotImplementedError as
part of the study session, then run the file again.
"""


# Warm-up: Hash Map and Binary Search

def two_sum(numbers, target):
    """Return indices of two numbers that add up to target, or []."""
    seen = {}
    for i, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return [seen[complement], i]
        seen[number] = i
    
    return []



def binary_search(numbers, target):
    """Return the index of target in sorted numbers, or -1 if it is absent."""
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

def max_sum_subarray_of_size_k(nums, k):
    start = 0
    currentSum = 0
    maxSum = float('-inf')

    for i in range(len(nums)):
        currentSum += nums[i]
        if i - start + 1 == k:
            maxSum = max(maxSum, currentSum)
            currentSum -= nums[start]
            start += 1
    
    return maxSum


# Mock interview #1: Sliding Window

def longest_substring_without_repeating_chars(text):
    """Return the length of the longest substring with no repeated characters."""
    left = 0
    seen = {}
    best = 0

    for right, char in enumerate(text):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        best = max(best, right - left + 1)

    return best    


# Mock interview #2: DFS/BFS

def number_of_islands(grid):
    """Return the number of horizontally or vertically connected islands."""
    
    if grid is None or len(grid) == 0:
        return 0

    islandCount = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, column):
        if (0 > row or row >= rows or 0 > column or column >= cols or grid[row][column] == "0"):
            return
        grid[row][column] = "0"
        dfs(row - 1, column)
        dfs(row + 1, column)
        dfs(row, column - 1)
        dfs(row, column + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islandCount += 1
                dfs(r, c)
    
    return islandCount


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3], 10) == []
    assert two_sum([], 5) == []


def test_binary_search():
    assert binary_search([], 9) == -1
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 1) == -1
    assert binary_search([1, 2, 2, 2, 3], 2) in {1, 2, 3}

def test_max_sum_array():
    assert max_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_subarray_of_size_k([100, 200, 300, 400], 2) == 700
    assert max_sum_subarray_of_size_k([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39


def test_longest_substring_without_repeating_chars():
    assert longest_substring_without_repeating_chars("") == 0
    assert longest_substring_without_repeating_chars("abcabcbb") == 3
    assert longest_substring_without_repeating_chars("bbbbb") == 1
    assert longest_substring_without_repeating_chars("pwwkew") == 3
    assert longest_substring_without_repeating_chars("dvdf") == 3
    assert longest_substring_without_repeating_chars(" ") == 1
    assert longest_substring_without_repeating_chars("abba") == 2


def test_number_of_islands():
    assert number_of_islands([]) == 0
    assert number_of_islands([["0"]]) == 0
    assert number_of_islands([["1"]]) == 1
    assert number_of_islands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    ) == 1
    assert number_of_islands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    ) == 3
    assert number_of_islands(
        [
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"],
        ]
    ) == 5


def run_tests():
    tests = [
        test_two_sum,
        test_binary_search,
        test_max_sum_array,
        test_longest_substring_without_repeating_chars,
        test_number_of_islands,
    ]
    for test in tests:
        test()
        print(f"PASS: {test.__name__}")
    print("All Day 2 tests passed.")


if __name__ == "__main__":
    run_tests()
