"""
Given a string s, determine whether it is a palindrome after ignoring
non-alphanumeric characters and case.

Example:
"A man, a plan, a canal: Panama" -> True

How to test this:
pytest -q reference_tests -k valid_palindrome
# or
pytest -q reference_tests/test_reference_solutions.py -k valid_palindrome
"""


def valid_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True
