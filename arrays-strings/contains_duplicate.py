"""
Given an integer array nums, return True if any value appears at least twice,
and False if every element is distinct.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

Example:
nums = [1, 2, 3, 1]
return True

How to test this:
pytest -q reference_tests -k contains_duplicate
# or
pytest -q reference_tests/test_reference_solutions.py -k contains_duplicate
"""


def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False
