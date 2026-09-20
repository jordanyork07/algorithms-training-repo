# Linked Lists

This topic focuses on pointer manipulation and cycle detection. The key idea is to work with node relationships rather than array indices, while keeping track of the important references you need to preserve.

## Problems in this folder
1. remove_nth_from_end
   - Delete the node that is n positions from the end of a singly linked list.
   - Typical interview cues: dummy head, fast/slow pointer, careful edge cases.
2. has_cycle
   - Determine whether a linked list contains a cycle.
   - Typical interview cues: tortoise and hare, repeated iteration, visited references.
3. reverse_linked_list
   - Reverse a singly linked list in place and return the new head.
   - Typical interview cues: pointer rewiring, tracking previous and next references.

## What to practice
- Dummy head nodes
- Fast/slow pointer reasoning
- Updating next pointers without losing access to the rest of the list
- Reversing pointer relationships while preserving traversal state
