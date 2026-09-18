# Recursion and Backtracking

This topic focuses on exploring choices systematically while keeping track of the current state. The main pattern is: choose one option, recurse, then undo the choice before trying another branch.

## Problems in this folder
1. subsets
   - Generate every subset of a list of distinct integers.
   - Typical interview cues: DFS branch and bound, decision tree, result accumulation.
2. combination_sum
   - Find all unique combinations of candidates whose sum equals a target.
   - Typical interview cues: recursion, pruning, avoiding duplicate branches.

## What to practice
- Base-case design
- State restoration after recursion
- Ordering choices to make pruning and duplicates easier to reason about
