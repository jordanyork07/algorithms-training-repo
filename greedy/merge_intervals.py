"""
Given a list of intervals, where each interval is [start, end], merge all
overlapping intervals and return the merged result in ascending order by start.

Constraints:
- 1 <= len(intervals) <= 10^4
- intervals[i] is a pair of integers.
- The intervals may overlap or touch at a boundary.

Example:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
return [[1, 6], [8, 10], [15, 18]]

How to test this:
pytest -q reference_tests -k merge_intervals
# or
pytest -q reference_tests/test_reference_solutions.py -k merge_intervals
"""


def merge_intervals(intervals):
    raise NotImplementedError("Implement this function.")
