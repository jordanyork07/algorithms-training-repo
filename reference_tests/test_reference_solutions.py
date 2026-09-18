import importlib.util
from pathlib import Path


def load_module(topic, name):
    path = Path(__file__).resolve().parents[1] / topic / f"{name}.solution.py"
    spec = importlib.util.spec_from_file_location(f"{topic}_{name}_solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_contains_duplicate_reference():
    module = load_module("arrays-strings", "contains_duplicate")
    assert module.contains_duplicate([1, 2, 3, 1]) is True
    assert module.contains_duplicate([1, 2, 3, 4]) is False


def test_group_anagrams_reference():
    module = load_module("arrays-strings", "group_anagrams")
    result = module.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(map(sorted, result)) == [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]


def test_two_sum_reference():
    module = load_module("hashmaps", "two_sum")
    assert module.two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_pair_with_target_sum_reference():
    module = load_module("two-pointers-sliding-window", "pair_with_target_sum")
    assert module.pair_with_target_sum([1, 2, 3, 4, 6], 6) == [1, 3]


def test_longest_substring_without_repeating_chars_reference():
    module = load_module("two-pointers-sliding-window", "longest_substring_without_repeating_chars")
    assert module.longest_substring_without_repeating_chars("abcabcbb") == 3


def test_climbing_stairs_reference():
    module = load_module("dynamic-programming", "climbing_stairs")
    assert module.climbing_stairs(2) == 2
    assert module.climbing_stairs(3) == 3


def test_binary_search_reference():
    module = load_module("sorting-searching", "binary_search")
    assert module.binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert module.binary_search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_can_jump_reference():
    module = load_module("greedy", "can_jump")
    assert module.can_jump([2, 3, 1, 1, 4]) is True


def test_merge_intervals_reference():
    module = load_module("greedy", "merge_intervals")
    assert module.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
