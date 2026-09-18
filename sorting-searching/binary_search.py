"""
Given a sorted array of integers nums and a target value, return the index of the
target if it exists in the array. If the target is not present, return -1.

Constraints:
- len(nums) <= 10^5
- nums is sorted in ascending order.
- -10^9 <= nums[i] <= 10^9

Example:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
return 4

How to test this:
pytest -q reference_tests -k binary_search
# or
pytest -q reference_tests/test_reference_solutions.py -k binary_search
"""


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
