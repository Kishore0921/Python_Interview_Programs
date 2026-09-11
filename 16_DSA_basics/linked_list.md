# Linked List

## What is a Linked List?

A linked list is a linear data structure made up of a chain of **nodes**,
where each node stores a value and a reference (or "pointer") to the
next node in the sequence. Unlike arrays, linked list elements are not
stored in contiguous memory — they can live anywhere in memory, linked
together only by these references.

## Key Characteristics

- **Non-contiguous memory**: Nodes can be scattered anywhere in memory;
  only the pointers connect them.
- **Sequential access only**: To reach the nth node, you must traverse
  from the head, following pointers one by one — there is no direct
  indexing like `list[n]`.
- **Dynamic size**: Growing or shrinking a linked list doesn't require
  resizing or copying, unlike a traditional fixed-size array.
- **Each node** typically contains:
  - `data`: the value stored
  - `next`: a reference to the next node (and `prev` in a doubly linked
    list)

## Types of Linked Lists

- **Singly Linked List**: Each node points only to the *next* node.
  Traversal is one-directional (head → tail).
- **Doubly Linked List**: Each node points to both the *next* and the
  *previous* node, allowing traversal in both directions at the cost of
  extra memory per node.
- **Circular Linked List**: The last node points back to the first node
  instead of pointing to `None`, forming a loop. This can be singly or
  doubly linked.

## Core Operations and Their Time Complexity

| Operation | Description | Time Complexity |
|-----------|--------------|------------------|
| Access (by index) | Get the nth element | O(n) |
| Search | Find if a value exists | O(n) |
| Insertion (at head) | Add a new node at the beginning | O(1) |
| Insertion (at tail) | Add a new node at the end | O(n), or O(1) if a tail pointer is maintained |
| Insertion (middle) | Add a node after a known node | O(1) once the position is found, O(n) to find it |
| Deletion (at head) | Remove the first node | O(1) |
| Deletion (at tail) | Remove the last node | O(n) for singly linked, O(1) for doubly linked with a tail pointer |
| Traversal | Visit every node | O(n) |

## Linked List vs Array

| Aspect | Array | Linked List |
|--------|-------|-------------|
| Memory layout | Contiguous | Scattered (linked via pointers) |
| Access by index | O(1) | O(n) |
| Insertion/deletion at start | O(n) | O(1) |
| Insertion/deletion at end | O(1) amortized | O(n) (or O(1) with tail pointer) |
| Memory overhead | Minimal (just the data) | Extra memory per node for pointer(s) |
| Cache performance | Better (contiguous memory) | Worse (scattered memory) |

## Real-World and Programming Uses

- **Implementing other data structures**: Stacks, queues, and hash map
  buckets (for collision handling) are often built on linked lists.
- **Music/video playlists**: A doubly linked list naturally models
  "next" and "previous" track navigation.
- **Undo history with flexible navigation**: Where you need to move
  both forward and backward through states.
- **Memory-efficient insertion/deletion**: Useful when the number of
  insertions/deletions at arbitrary positions is high relative to the
  number of lookups by index.

## Why Linked Lists Matter in Interviews

Linked lists are one of the most common interview topics because they
test pointer manipulation and edge-case handling: reversing a linked
list, detecting a cycle (Floyd's cycle detection / "tortoise and hare"),
finding the middle element, merging two sorted linked lists, and
removing the nth node from the end are all classic problems.

## Advantages

- Dynamic size — grows and shrinks without resizing/copying
- Efficient insertion/deletion at the head (and anywhere, once you have
  a reference to the position)
- No wasted pre-allocated memory, unlike some array implementations

## Disadvantages

- No random access — accessing an arbitrary element requires traversal
- Extra memory overhead for storing pointers in each node
- Poorer cache locality compared to arrays, since nodes are scattered in
  memory
- More complex to implement and debug (pointer manipulation is
  error-prone)