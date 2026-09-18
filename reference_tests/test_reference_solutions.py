import importlib.util
from pathlib import Path


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def load_module(topic, name, reference=False):
    suffix = ".solution.py" if reference else ".py"
    path = Path(__file__).resolve().parents[1] / topic / f"{name}{suffix}"
    module_kind = "solution" if reference else "practice"
    spec = importlib.util.spec_from_file_location(f"{topic}_{name}_{module_kind}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def as_linked_list(values):
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def linked_list_to_list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


def tree_from_list(values):
    if not values:
        return None

    def build(index):
        if index >= len(values) or values[index] is None:
            return None
        return TreeNode(values[index], build(index * 2 + 1), build(index * 2 + 2))

    return build(0)


def test_contains_duplicate_practice():
    module = load_module("arrays-strings", "contains_duplicate")
    assert module.contains_duplicate([]) is False
    assert module.contains_duplicate([1, 2, 3, 1]) is True
    assert module.contains_duplicate([1, 2, 3, 4]) is False
    assert module.contains_duplicate([5, 5, 5]) is True


def test_group_anagrams_practice():
    module = load_module("arrays-strings", "group_anagrams")
    assert module.group_anagrams([]) == []
    result = module.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(map(sorted, result)) == [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
    result = module.group_anagrams(["", ""])
    assert len(result) == 1 and sorted(result[0]) == ["", ""]


def test_two_sum_practice():
    module = load_module("hashmaps", "two_sum")
    assert module.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert module.two_sum([3, 2, 4], 6) == [1, 2]
    assert module.two_sum([1, 2, 3], 10) == []


def test_top_k_frequent_practice():
    module = load_module("hashmaps", "top_k_frequent")
    assert module.top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert module.top_k_frequent([1], 1) == [1]
    assert set(module.top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2)) == {-1, 2}


def test_pair_with_target_sum_practice():
    module = load_module("two-pointers-sliding-window", "pair_with_target_sum")
    assert module.pair_with_target_sum([1, 2, 3, 4, 6], 6) == [1, 3]
    assert module.pair_with_target_sum([2, 3, 4], 6) == [0, 2]
    assert module.pair_with_target_sum([1, 2, 3], 9) == []


def test_longest_substring_without_repeating_chars_practice():
    module = load_module("two-pointers-sliding-window", "longest_substring_without_repeating_chars")
    assert module.longest_substring_without_repeating_chars("") == 0
    assert module.longest_substring_without_repeating_chars("abcabcbb") == 3
    assert module.longest_substring_without_repeating_chars("bbbbb") == 1
    assert module.longest_substring_without_repeating_chars("pwwkew") == 3


def test_climbing_stairs_practice():
    module = load_module("dynamic-programming", "climbing_stairs")
    assert module.climbing_stairs(1) == 1
    assert module.climbing_stairs(2) == 2
    assert module.climbing_stairs(3) == 3
    assert module.climbing_stairs(5) == 8


def test_house_robber_practice():
    module = load_module("dynamic-programming", "house_robber")
    assert module.house_robber([]) == 0
    assert module.house_robber([1, 2, 3, 1]) == 4
    assert module.house_robber([2, 7, 9, 3, 1]) == 12
    assert module.house_robber([0, 0, 0]) == 0


def test_binary_search_practice():
    module = load_module("sorting-searching", "binary_search")
    assert module.binary_search([], 9) == -1
    assert module.binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert module.binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert module.binary_search([1, 2, 2, 2, 3], 2) in {1, 2, 3}


def test_koko_eating_bananas_practice():
    module = load_module("sorting-searching", "koko_eating_bananas")
    assert module.koko_eating_bananas([3, 6, 7, 11, 12], 8) == 6
    assert module.koko_eating_bananas([30, 11, 23, 4, 20], 5) == 30
    assert module.koko_eating_bananas([1000000000], 1) == 1000000000


def test_can_jump_practice():
    module = load_module("greedy", "can_jump")
    assert module.can_jump([0]) is True
    assert module.can_jump([2, 3, 1, 1, 4]) is True
    assert module.can_jump([3, 2, 1, 0, 4]) is False
    assert module.can_jump([1, 1, 1, 0]) is True


def test_merge_intervals_practice():
    module = load_module("greedy", "merge_intervals")
    assert module.merge_intervals([]) == []
    assert module.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert module.merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert module.merge_intervals([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]


def test_valid_parentheses_practice():
    module = load_module("stacks-queues", "valid_parentheses")
    assert module.valid_parentheses("") is True
    assert module.valid_parentheses("()") is True
    assert module.valid_parentheses("([{}])") is True
    assert module.valid_parentheses("([)]") is False
    assert module.valid_parentheses("(") is False


def test_daily_temperatures_practice():
    module = load_module("stacks-queues", "daily_temperatures")
    assert module.daily_temperatures([]) == []
    assert module.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert module.daily_temperatures([1, 2, 3]) == [1, 1, 0]


def test_remove_nth_from_end_practice():
    module = load_module("linked-lists", "remove_nth_from_end")
    head = as_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(module.remove_nth_from_end(head, 2)) == [1, 2, 3, 5]
    head = as_linked_list([1])
    assert linked_list_to_list(module.remove_nth_from_end(head, 1)) == []
    head = as_linked_list([1, 2])
    assert linked_list_to_list(module.remove_nth_from_end(head, 1)) == [1]


def test_has_cycle_practice():
    module = load_module("linked-lists", "has_cycle")
    assert module.has_cycle(None) is False
    assert module.has_cycle(as_linked_list([1, 2, 3, 4])) is False
    head = as_linked_list([3, 2, 0, -4])
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = head.next
    assert module.has_cycle(head) is True


def test_max_depth_binary_tree_practice():
    module = load_module("trees-graphs", "max_depth_binary_tree")
    assert module.max_depth_binary_tree(None) == 0
    root = tree_from_list([3, 9, 20, None, None, 15, 7])
    assert module.max_depth_binary_tree(root) == 3
    root = tree_from_list([1, None, 2])
    assert module.max_depth_binary_tree(root) == 2


def test_number_of_islands_practice():
    module = load_module("trees-graphs", "number_of_islands")
    assert module.number_of_islands([]) == 0
    grid = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert module.number_of_islands(grid) == 1
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    assert module.number_of_islands(grid) == 3


def test_subsets_practice():
    module = load_module("recursion-backtracking", "subsets")
    assert module.subsets([]) == [[]]
    result = module.subsets([1, 2, 3])
    assert sorted(map(tuple, result)) == [(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]


def test_combination_sum_practice():
    module = load_module("recursion-backtracking", "combination_sum")
    assert module.combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    result = module.combination_sum([2, 3], 1)
    assert result == []
    result = module.combination_sum([2, 3], 5)
    assert sorted(map(tuple, result)) == [(2, 3)]
