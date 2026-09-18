"""Reference solution for subsets."""


def subsets(nums):
    result = []

    def dfs(index, path):
        result.append(path.copy())
        for i in range(index, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    return result
