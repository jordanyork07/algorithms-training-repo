"""
Given a sorted array of integers nums and a target value, find a pair of indices
(i, j) such that nums[i] + nums[j] == target.

Return the pair as [left_index, right_index]. If no such pair exists, return []
(or another explicit sentinel if the platform requires one).

Constraints:
- 2 <= len(nums) <= 10^5
- nums is sorted in non-decreasing order.
- -10^9 <= nums[i] <= 10^9

Example:
nums = [1, 2, 3, 4, 6]
target = 6
return [1, 3]

How to test this:
pytest -q reference_tests -k pair_with_target_sum
# or
pytest -q reference_tests/test_reference_solutions.py -k pair_with_target_sum
"""


def pair_with_target_sum(nums, target):
    for i in nums:
        difference = target - i
        if difference in nums:
            indexI = nums.index(i)
            indexDifference = nums.index(difference)

            return [indexI, indexDifference] if indexI < indexDifference else [indexDifference, indexI]

    return []
