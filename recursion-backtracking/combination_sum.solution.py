"""Reference solution for combination_sum."""


def combination_sum(candidates, target):
    result = []

    def dfs(start, remaining, path):
        if remaining == 0:
            result.append(path.copy())
            return
        if remaining < 0:
            return
        for index in range(start, len(candidates)):
            path.append(candidates[index])
            dfs(index, remaining - candidates[index], path)
            path.pop()

    dfs(0, target, [])
    return result
