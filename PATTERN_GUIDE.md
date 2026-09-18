# Pattern Recognition Guide

This is a quick way to identify which category a problem likely belongs to.

## Arrays and strings
Use when the problem involves scanning, partitioning, or comparing positions in ordered data.

Typical patterns:
- prefix sums
- two pointers
- sliding window
- string frequency counting

## Hash maps
Use when the problem involves counting, grouping, or finding a complement.

Typical patterns:
- counts by value
- frequency tables
- set membership checks
- two-sum style problems

## Two pointers
Use when the data is sorted or partially ordered and a left/right scan helps maintain an invariant.

Typical patterns:
- sorted pair search
- move pointers inward
- partitioning or shrinking windows

## Sliding window
Use when you are asked for the longest or shortest subarray or substring satisfying a condition.

Typical signals:
- contiguous segment
- maximize/minimize window size
- maintain a condition while adding/removing elements

## Binary search
Use when the answer space is monotonic and you can check whether a mid-point is feasible.

Typical signals:
- sorted array
- minimum valid speed
- check a property over a range

## BFS / DFS
Use when the problem involves graph or tree traversal, connected components, or shortest paths in unweighted graphs.

Typical signals:
- neighbor exploration
- distance or reachability
- components or island counting

## Greedy
Use when a locally optimal choice can be shown to lead to the global optimum.

Typical signals:
- interval merging
- scheduling or selection
- maximum coverage with simple rules

## Dynamic programming
Use when the problem can be decomposed into overlapping subproblems and a small state.

Typical signals:
- repeated work
- best path / best count / best profit
- decisions depending on previous state

## Backtracking
Use when you need to generate combinations, subsets, or permutations while exploring choices.

Typical signals:
- all valid combinations
- choose/explore/unchoose recursion
- pruning based on feasibility

## Stacks and queues
Use when order matters and you need to process items relative to earlier or later elements.

Typical signals:
- matching parentheses
- next greater element
- monotonic stack patterns

## Linked lists
Use when you are manipulating pointer relationships instead of array indexing.

Typical signals:
- reverse or merge nodes
- detect cycles
- remove from end

## Trees and graphs
Use when the data is hierarchical or connected and the solution depends on traversal.

Typical signals:
- tree height
- connected components
- path existence

## What to say in an interview
When stuck, a strong default phrasing is:

- “I can see a brute-force approach, but I want to remove the repeated work.”
- “The key invariant here is…”
- “This looks like a monotonic condition, so I’m checking whether binary search applies.”
- “I’m exploring the state space to see if this is a DP or backtracking problem.”
