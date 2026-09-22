#!/usr/bin/env python3
"""Reset the practice implementations in morePracticeWritingMethods.py.

Run from the repo root:
    python3 wipe_practice_methods.py

This keeps the function definitions and test cases, but replaces each
implementation body with a simple pass so you can re-implement them from scratch.
"""

from __future__ import annotations

import argparse
from pathlib import Path

PRACTICE_FUNCTIONS = [
    "two_sum",
    "contains_duplicate",
    "is_valid_anagram",
    "is_valid_palindrome",
    "max_profit",
    "length_of_longest_substring",
    "binary_search",
    "is_valid_parentheses",
    "max_depth",
    "reverse_linked_list",
    "number_of_islands",
    "merge_intervals",
    "linked_list_values",
]


def wipe_function(source: str, function_name: str) -> str:
    """Replace only the body of one function while keeping its definition intact."""
    lines = source.splitlines(keepends=True)

    for index, line in enumerate(lines):
        if line.startswith(f"def {function_name}("):
            start = index
            break
    else:
        return source

    header_end = start
    while header_end + 1 < len(lines) and not lines[header_end].strip().endswith(":"):
        header_end += 1

    end = len(lines)
    for index in range(header_end + 1, len(lines)):
        current = lines[index]
        if not current.strip():
            continue
        if current.startswith((" ", "\t")):
            continue
        stripped = current.strip()
        if stripped.startswith("def ") or stripped.startswith("class "):
            end = index
            break
        if stripped.startswith('if __name__ == "__main__":'):
            end = index
            break

    header = "".join(lines[start : header_end + 1])
    replacement = [header.rstrip() + "\n    pass\n\n"]
    return "".join(lines[:start] + replacement + lines[end:])


def wipe_practice_file(path: Path) -> None:
    source = path.read_text()
    for function_name in PRACTICE_FUNCTIONS:
        source = wipe_function(source, function_name)

    path.write_text(source)
    print(f"Cleared implementations in {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Replace practice method implementations with pass statements while preserving definitions and tests."
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parent / "morePracticeWritingMethods.py",
        help="Path to the Python file to reset. Defaults to morePracticeWritingMethods.py.",
    )
    args = parser.parse_args()

    wipe_practice_file(args.file)
