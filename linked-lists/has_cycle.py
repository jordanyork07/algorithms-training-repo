"""
Given a singly linked list, determine whether it contains a cycle.

The list may be empty or may contain a cycle. Return True if a cycle is present,
and False otherwise.

Constraints:
- 0 <= number of nodes <= 10^5

Example:
head = [3, 2, 0, -4]
position = 1
return True

Explanation:
The value at index 1 points back to the node containing -4, creating a cycle.

How to test this:
pytest -q reference_tests -k has_cycle
# or
pytest -q reference_tests/test_reference_solutions.py -k has_cycle
"""


def has_cycle(head):
    raise NotImplementedError("Implement this function.")
