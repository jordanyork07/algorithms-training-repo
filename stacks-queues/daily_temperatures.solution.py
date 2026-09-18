"""Reference solution for daily_temperatures."""


def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []
    for index, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            previous = stack.pop()
            result[previous] = index - previous
        stack.append(index)
    return result
