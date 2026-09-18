"""
Given an array of daily temperatures, return a list of the same length where each
entry indicates how many days you must wait before a warmer temperature appears.

If there is no future warmer temperature, the answer is 0.

Constraints:
- 1 <= len(temperatures) <= 10^5
- 30 <= temperatures[i] <= 100

Example:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
return [1, 1, 4, 2, 1, 1, 0, 0]

How to test this:
pytest -q reference_tests -k daily_temperatures
# or
pytest -q reference_tests/test_reference_solutions.py -k daily_temperatures
"""


def daily_temperatures(temperatures):
    raise NotImplementedError("Implement this function.")
