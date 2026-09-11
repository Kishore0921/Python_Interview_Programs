# Queue

## What is a Queue?

A queue is a linear data structure that follows the **FIFO (First In,
First Out)** principle — the first element added is the first one to be
removed. Think of a line of people waiting: the first person in line is
served first.

In Python, a queue is typically implemented using `collections.deque`
(efficient at both ends) or the built-in `queue.Queue` class (which also
adds thread-safety for concurrent programs).

## Key Characteristics

- **FIFO order**: The oldest element in the queue is the first to be
  removed.
- **Two access points**: Elements are added at the **rear** (enqueue)
  and removed from the **front** (dequeue).
- **No random access**: Like a stack, you can't directly access an
  element in the middle without removing the ones ahead of it.

## Core Operations and Their Time Complexity

| Operation | Description | Time Complexity |
|-----------|--------------|------------------|
| Enqueue | Add an element to the rear | O(1) |
| Dequeue | Remove and return the front element | O(1) |
| Peek / Front | View the front element without removing it | O(1) |
| isEmpty | Check whether the queue has no elements | O(1) |
| Search | Find if a value exists in the queue | O(n) |

**Note:** Using a plain Python `list` for a queue is inefficient because
removing from the front (`list.pop(0)`) is O(n), since all remaining
elements must shift left. `collections.deque` avoids this by supporting
O(1) operations at both ends.

## Types of Queues

- **Simple Queue**: The standard FIFO queue described above.
- **Circular Queue**: The rear wraps around to reuse freed-up space at
  the front once elements have been dequeued, avoiding wasted space in a
  fixed-size array implementation.
- **Priority Queue**: Elements are dequeued based on priority rather
  than order of insertion (commonly implemented with a heap, e.g.
  Python's `heapq`).
- **Deque (Double-Ended Queue)**: Allows insertion and removal from
  *both* the front and the rear, making it a more flexible structure
  than a simple queue.

## Real-World and Programming Uses

- **Task scheduling**: Operating systems use queues to manage processes
  waiting for CPU time.
- **Breadth-First Search (BFS)**: Graph and tree traversal algorithms
  use a queue to explore nodes level by level.
- **Print/job queues**: Print jobs or requests are handled in the order
  they arrive.
- **Buffering (e.g. streaming data, message queues)**: Data is queued
  up and processed in the order received.

## Why Queues Matter in Interviews

Queue-based problems commonly appear in graph/tree traversal (BFS),
simulation problems (e.g. modeling a ticket counter or task scheduler),
and design questions (e.g. "design a circular queue" or "implement a
queue using two stacks"). Interviewers use these to test understanding
of FIFO logic and awareness of the cost of using the wrong underlying
structure (like a plain list) for queue operations.

## Advantages

- Enqueue and dequeue are O(1) with the right underlying structure
  (`deque`)
- Naturally models real-world "waiting line" scenarios
- Forms the basis for many graph/tree traversal algorithms (BFS)

## Disadvantages

- No random access to elements in the middle
- A naive array-based implementation can degrade to O(n) dequeue
  operations if not implemented carefully (e.g. using a plain list)
- Fixed-size queue implementations need circular logic to avoid wasting
  space