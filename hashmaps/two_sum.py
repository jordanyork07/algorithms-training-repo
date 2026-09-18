"""
Given an array of integers nums and an integer target, return the indices of the
two numbers such that they add up to the target.

You may assume that each input has exactly one valid solution, and you cannot use
the same element twice.

Constraints:
- 2 <= len(nums) <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

Example:
nums = [2, 7, 11, 15]
target = 9
return [0, 1]

How to test this:
pytest -q reference_tests -k two_sum
# or
pytest -q reference_tests/test_reference_solutions.py -k two_sum
"""


def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return []
