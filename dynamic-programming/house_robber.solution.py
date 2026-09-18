"""Reference solution."""

def house_robber(nums):
    prev_two = 0
    prev_one = 0
    for value in nums:
        current = max(prev_one, prev_two + value)
        prev_two = prev_one
        prev_one = current
    return prev_one
