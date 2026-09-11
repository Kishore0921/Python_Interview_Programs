# Stack

## What is a Stack?

A stack is a linear data structure that follows the **LIFO (Last In,
First Out)** principle — the last element added is the first one to be
removed. Think of a stack of plates: you can only add or remove a plate
from the top.

In Python, a stack is commonly implemented using a `list` (with
`append()` and `pop()`) or `collections.deque` (preferred for better
performance on push/pop operations).

## Key Characteristics

- **LIFO order**: The most recently added element is the first to be
  removed.
- **Restricted access**: Elements can only be added or removed from one
  end, called the **top** of the stack.
- **No random access**: You cannot directly access an element in the
  middle of a stack without first removing the elements above it.

## Core Operations and Their Time Complexity

| Operation | Description | Time Complexity |
|-----------|--------------|------------------|
| Push | Add an element to the top | O(1) |
| Pop | Remove and return the top element | O(1) |
| Peek / Top | View the top element without removing it | O(1) |
| isEmpty | Check whether the stack has no elements | O(1) |
| Search | Find if a value exists in the stack | O(n) |

## How It's Typically Implemented

- **Using a list**: `stack.append(x)` to push, `stack.pop()` to pop.
  Simple, but insertion/removal from the *end* of a Python list is
  already O(1) amortized, so this works well.
- **Using `collections.deque`**: `deque.append(x)` to push,
  `deque.pop()` to pop. Preferred over a plain list in performance-
  sensitive code because deque is implemented as a doubly linked list of
  blocks, giving consistently fast O(1) operations at both ends.
- **Using a linked list**: Push/pop at the head of a linked list, giving
  O(1) operations without the resizing behavior of arrays.

## Real-World and Programming Uses

- **Function call stack**: Tracks function calls in a program; each
  call is "pushed" and returns are "popped."
- **Undo/Redo functionality**: The last action performed is the first
  one undone.
- **Expression evaluation**: Used to evaluate postfix/prefix expressions
  and to check balanced parentheses/brackets.
- **Backtracking algorithms**: Used to keep track of choices made so
  they can be undone (e.g. maze solving, DFS traversal).
- **Browser history (back button)**: The last page visited is the first
  one you go back to.

## Why Stacks Matter in Interviews

Stack-based problems are extremely common in interviews:
balanced-parentheses checking, evaluating expressions, implementing a
"min stack," reversing a string/list, and simulating recursion
iteratively. Interviewers use these to test understanding of LIFO logic
and the ability to translate a recursive idea into an iterative one
using an explicit stack.

## Advantages

- Simple to implement and reason about
- All core operations (push, pop, peek) are O(1)
- Naturally models problems that involve "undoing" the most recent step

## Disadvantages

- No random access to elements — only the top is directly accessible
- Limited use cases outside of LIFO-order problems
- Can lead to stack overflow if used unbounded in recursive contexts