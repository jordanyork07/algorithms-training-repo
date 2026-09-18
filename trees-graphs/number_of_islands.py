"""
Given a binary grid with '1' as land and '0' as water, return the number of islands.

An island is a group of connected land cells that are adjacent horizontally or
vertically. Diagonal connections do not count.

Constraints:
- 1 <= rows, cols <= 300

Example:
grid = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
return 1

How to test this:
pytest -q reference_tests -k number_of_islands
# or
pytest -q reference_tests/test_reference_solutions.py -k number_of_islands
"""


def number_of_islands(grid):
    raise NotImplementedError("Implement this function.")
