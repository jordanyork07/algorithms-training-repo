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
    left = 0
    seen = {}
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
