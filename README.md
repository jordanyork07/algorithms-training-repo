# Algorithm Interview Practice Repository

This repository is set up for Python-based algorithm interview practice. The structure is intentionally split into practice folders and a reference testing flow so you can solve the problems first, then validate against known-good implementations.

## Topics
- arrays-strings
- hashmaps
- two-pointers-sliding-window
- stacks-queues
- linked-lists
- trees-graphs
- recursion-backtracking
- dynamic-programming
- sorting-searching
- greedy

## Workflow
1. Open a practice file in any topic folder.
2. Implement the stubbed function from scratch.
3. Run the relevant test file for that practice module when ready.
4. Use the matching .solution.py file or the `reference_tests/` suite as a validation reference.

## Commands
```bash
python3 -m pip install -U pip
python3 -m pip install -e '.[dev]'
pytest reference_tests -q
```
