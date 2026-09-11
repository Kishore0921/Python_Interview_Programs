# Arrays

## What is an Array?

An array is a collection of elements, all of the same type, stored in
contiguous memory locations. Each element can be accessed directly using
an index, which makes arrays one of the most fundamental and widely used
data structures.

In Python, the built-in `list` behaves like a dynamic array — it can grow
or shrink in size and hold elements of any type, though for strict
"array" behavior (fixed type, more memory-efficient), Python also
provides the `array` module and libraries like NumPy.

## Key Characteristics

- **Fixed vs Dynamic size**: Traditional arrays (in languages like C/Java)
  have a fixed size set at creation. Python lists are dynamic — they
  resize automatically as elements are added or removed.
- **Contiguous memory**: Elements are stored next to each other in
  memory, which enables fast, constant-time access by index.
- **Homogeneous (traditionally)**: Classic arrays hold elements of a
  single type. Python lists relax this and can hold mixed types.
- **Zero-indexed**: The first element is at index 0.

## Common Operations and Their Time Complexity

| Operation | Description | Time Complexity |
|-----------|--------------|------------------|
| Access | Get element at a given index | O(1) |
| Search (unsorted) | Find if a value exists | O(n) |
| Search (sorted, binary search) | Find if a value exists | O(log n) |
| Insertion (at end) | Add an element at the end | O(1) amortized |
| Insertion (at beginning/middle) | Add an element at a specific position | O(n) |
| Deletion (at end) | Remove the last element | O(1) |
| Deletion (at beginning/middle) | Remove from a specific position | O(n) |
| Traversal | Visit every element | O(n) |

Insertion/deletion at the end is cheap because no other elements need to
shift. Insertion/deletion elsewhere is expensive because all subsequent
elements must shift to fill or make a gap.

## Types of Arrays

- **One-Dimensional (1D) Array**: A simple linear list of elements,
  e.g. `[10, 20, 30, 40]`.
- **Multi-Dimensional Array**: An array of arrays, commonly used to
  represent grids, matrices, or tables, e.g. a 2D array representing a
  matrix: `[[1, 2], [3, 4]]`.
- **Dynamic Array**: An array that automatically resizes when it runs
  out of space (this is how Python's `list` works internally — it
  over-allocates memory and grows in chunks to keep amortized insertion
  at O(1)).

## Why Arrays Matter in Interviews

Arrays are the foundation for a huge number of interview problems:
searching, sorting, sliding window techniques, two-pointer techniques,
prefix sums, and more. Interviewers often use arrays to test:

- Understanding of indexing and bounds
- Ability to reason about time/space trade-offs
- Recognizing when an array is the right structure vs. a different one
  (e.g. a linked list, when frequent insertions/deletions in the middle
  are needed)

## Advantages

- Fast, constant-time access to any element by index
- Simple and memory-efficient for storing a fixed collection of items
- Good cache locality due to contiguous memory storage

## Disadvantages

- Fixed size in traditional/static arrays (can't grow beyond allocated
  memory without creating a new array)
- Costly insertions/deletions in the middle or at the beginning, since
  elements must shift
- Wasted space if the array is over-allocated, or repeated
  resizing/copying overhead in dynamic arrays