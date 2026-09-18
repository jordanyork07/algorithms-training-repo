# Algorithm Interview Practice Repository

This repository is designed for a live coding interview in which you are expected to reason out loud, identify the right problem structure, and produce a clean solution under time pressure.

## Interview format this repo is tuned for
- 5 minutes introduction
- 40 minutes coding exercise
- 15 minutes buffer for conversation and wrap-up
- Virtual interview via Google Meet
- You may use Google, GitHub, or language documentation for syntax or ideas
- You may not use AI tools to derive the solution

The repo is intentionally structured for a realistic interview loop: solve, think aloud, verify, and refine without leaning on a prewritten answer.

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
3. Think through the invariant and constraints out loud as you work.
4. Validate the result with the matching solution file or the reference test suite.
5. Re-solve from a blank file after a short break.

## Interview-specific preparation checklist
- Test microphone, camera, and internet before the session
- Prepare a simple editor with a single blank file ready to use
- Keep one scratch pad or notes file open for clarifying questions and edge cases
- Use a language you are comfortable with; Python is a good default here
- Practice saying your reasoning out loud while solving
- Keep the solution readable and structured instead of squeezing everything into one dense block
- Ask clarifying questions early when the prompt is ambiguous

## Commands
```bash
python3 -m pip install -U pip
python3 -m pip install -e '.[dev]'
pytest reference_tests -q
```

## Run one problem at a time
You do not need to read every assertion in every problem file. Use pytest’s `-k` selector to run just the reference check for a single problem.

```bash
# run only the contains_duplicate reference test
pytest -q reference_tests -k contains_duplicate

# run only the two_sum reference test
pytest -q reference_tests -k two_sum

# run only the binary_search reference test
pytest -q reference_tests -k binary_search
```

You can also run the entire suite whenever you want a broader sanity check.

## Best interview behaviors
- Start by restating the problem in your own words
- Mention the input/output contract and key constraints
- Discuss a brute-force approach before optimising
- Call out the bottleneck and why the improved approach helps
- State the complexity before you code
- Test the obvious edge cases before finishing
- Explain the trade-offs if you are choosing between simpler and faster solutions
