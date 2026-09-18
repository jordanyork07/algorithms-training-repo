"""Reference solution."""

def can_jump(nums):
    max_reach = 0
    for index, value in enumerate(nums):
        if index > max_reach:
            return False
        max_reach = max(max_reach, index + value)
    return True
