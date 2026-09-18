"""
Given a string s containing only the characters '(', ')', '{', '}', '[', and ']',
determine whether the input string is valid.

A valid string has every opening bracket closed by the matching closing bracket in
the correct order.

Constraints:
- 0 <= len(s) <= 10^4

Example:
s = "([)]"
return False

How to test this:
pytest -q reference_tests -k valid_parentheses
# or
pytest -q reference_tests/test_reference_solutions.py -k valid_parentheses
"""


def valid_parentheses(s):
    raise NotImplementedError("Implement this function.")
