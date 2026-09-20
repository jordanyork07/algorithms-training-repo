"""
Given the head of a singly linked list, reverse the list and return the new head.

Example:
1 -> 2 -> 3 -> 4 -> None becomes 4 -> 3 -> 2 -> 1 -> None

How to test this:
pytest -q reference_tests -k reverse_linked_list
# or
pytest -q reference_tests/test_reference_solutions.py -k reverse_linked_list
"""


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
