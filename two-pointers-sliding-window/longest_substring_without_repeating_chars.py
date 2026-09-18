"""
Given a string s, find the length of the longest substring without repeating
characters.

Return the maximum number of consecutive, unique characters in any substring.

Constraints:
- 0 <= len(s) <= 5 * 10^4
- s consists of English letters, digits, symbols, and spaces.

Example:
 s = "abcabcbb"
 return 3

How to test this:
pytest -q reference_tests -k longest_substring_without_repeating_chars
# or
pytest -q reference_tests/test_reference_solutions.py -k longest_substring_without_repeating_chars
"""


def longest_substring_without_repeating_chars(s):
    raise NotImplementedError("Implement this function.")
