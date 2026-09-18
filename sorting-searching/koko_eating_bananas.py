"""
Koko loves bananas and wants to eat them at a fixed speed. Each pile in piles[i]
contains bananas, and Koko can eat at most speed bananas per hour.

If Koko eats too slowly, she may not finish all piles before h hours. Return the
minimum integer speed that allows her to finish all bananas within h hours.

Constraints:
- 1 <= len(piles) <= 10^4
- 1 <= h <= 10^9
- 1 <= piles[i] <= 10^9

Example:
piles = [3, 6, 7, 11, 12]
h = 8
return 4

How to test this:
pytest -q reference_tests -k koko_eating_bananas
# or
pytest -q reference_tests/test_reference_solutions.py -k koko_eating_bananas
"""


def koko_eating_bananas(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        hours = sum((pile + mid - 1) // mid for pile in piles)
        if hours <= h:
            right = mid
        else:
            left = mid + 1
    return left


