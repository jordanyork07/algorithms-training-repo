"""
Given two strings s and t, return True if t is an anagram of s.

Constraints:
- 0 <= len(s), len(t) <= 10^5
- Strings contain lowercase English letters.

Example:
s = "anagram"
t = "nagaram"
return True

How to test this:
pytest -q reference_tests -k valid_anagram
# or
pytest -q reference_tests/test_reference_solutions.py -k valid_anagram
"""


def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] == 0:
            del counts[ch]

    return not counts
