"""
Given a singly linked list and an integer n, remove the n-th node from the end of
the list and return the updated head.

The list is represented as a Python list of values for practice purposes.

Constraints:
- 1 <= n <= len(head)

Example:
head = [1, 2, 3, 4, 5]
n = 2
return [1, 2, 3, 5]

How to test this:
pytest -q reference_tests -k remove_nth_from_end
# or
pytest -q reference_tests/test_reference_solutions.py -k remove_nth_from_end
"""


def remove_nth_from_end(head, n):
    raise NotImplementedError("Implement this function.")
