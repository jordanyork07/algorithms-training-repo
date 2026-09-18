"""
Given an integer array nums and an integer k, return the k most frequent elements.

Your output can be in any order, unless the prompt explicitly requires a fixed
ordering. The important part is that the result contains the elements with the
highest frequency.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= k <= len(nums)
- -10^4 <= nums[i] <= 10^4

Example:
nums = [1, 1, 1, 2, 2, 3]
k = 2
return [1, 2]

How to test this:
pytest -q reference_tests -k top_k_frequent
# or
pytest -q reference_tests/test_reference_solutions.py -k top_k_frequent
"""


def top_k_frequent(nums, k):
    raise NotImplementedError("Implement this function.")
