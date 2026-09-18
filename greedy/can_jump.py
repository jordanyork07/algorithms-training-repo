"""
You are given an array of non-negative integers nums, where each element represents
the maximum number of steps you can move forward from that position.

Return True if you can reach the last index, or False otherwise.

Constraints:
- 1 <= len(nums) <= 10^5
- 0 <= nums[i] <= 10^5

Example:
nums = [2, 3, 1, 1, 4]
return True

How to test this:
pytest -q reference_tests -k can_jump
# or
pytest -q reference_tests/test_reference_solutions.py -k can_jump
"""


def can_jump(nums):
    raise NotImplementedError("Implement this function.")
