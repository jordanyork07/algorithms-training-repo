"""
Given an array of strings, group the anagrams together. Two strings are anagrams
if they have the same letters in the same frequency, regardless of order.

Return a list of groups, where each group contains strings that are anagrams of
one another. The order of the groups and the order of the strings within each
group can vary unless the platform specifies a fixed ordering.

Constraints:
- 0 <= len(strs) <= 10^4
- 0 <= len(s) <= 100
- All strings contain lowercase English letters.

Example:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
return [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

How to test this:
pytest -q reference_tests -k group_anagrams
# or
pytest -q reference_tests/test_reference_solutions.py -k group_anagrams
"""


def group_anagrams(strs):
    groups = {}
    for word in strs:
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
