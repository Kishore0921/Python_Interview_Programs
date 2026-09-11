# Hashing

## What is Hashing?

Hashing is a technique for mapping data of arbitrary size to a fixed-size
value (called a **hash code** or **hash value**) using a **hash
function**. This hash value is then used as an index into an underlying
array (often called a **hash table** or **hash map**), enabling very
fast lookup, insertion, and deletion.

In Python, the built-in `dict` and `set` types are implemented using
hash tables, which is why key lookups in a dictionary are, on average,
O(1) regardless of how many items it contains.

## Key Characteristics

- **Hash function**: A function that converts a key (e.g. a string,
  number, or object) into an integer index. A good hash function
  distributes keys uniformly across the available slots ("buckets") to
  minimize collisions.
- **Buckets**: The slots in the underlying array where values are
  stored, determined by the hash of the key.
- **Collisions**: Two different keys can sometimes produce the same hash
  index. Hash tables must handle this gracefully (see below).
- **Load factor**: The ratio of stored elements to the total number of
  buckets. When this gets too high, the table is resized ("rehashed")
  to maintain performance.

## Handling Collisions

- **Chaining**: Each bucket holds a list (or linked list) of all
  key-value pairs that hash to that index. On collision, the new pair is
  simply appended to the bucket's list.
- **Open Addressing**: On collision, the algorithm probes for the next
  available slot in the array itself (e.g. linear probing, quadratic
  probing, or double hashing), rather than storing a list per bucket.

## Core Operations and Their Time Complexity

| Operation | Description | Average Case | Worst Case |
|-----------|--------------|---------------|-------------|
| Insert | Add a key-value pair | O(1) | O(n) |
| Search | Look up a value by key | O(1) | O(n) |
| Delete | Remove a key-value pair | O(1) | O(n) |

The worst case (O(n)) occurs when many keys collide into the same
bucket (e.g. due to a poor hash function or adversarial input), turning
lookups into a linear search through that bucket.

## Real-World and Programming Uses

- **Dictionaries / Maps**: Python's `dict`, Java's `HashMap`, and
  similar structures across languages are all hash-table based.
- **Sets**: Used for fast membership testing and removing duplicates
  (Python's `set` is a hash table storing only keys, no values).
- **Caching**: Hash tables back many caching systems (e.g. memoization,
  LRU caches) for O(1) average lookup of previously computed results.
- **Database indexing**: Some database indexes use hashing for fast
  equality lookups.
- **Checksums and data integrity**: Cryptographic hash functions (a
  different, security-focused kind of hashing) verify that data hasn't
  been tampered with.

## Why Hashing Matters in Interviews

Hashing is one of the highest-leverage topics in interviews because so
many problems can be solved in O(n) time using a hash map instead of a
naive O(n²) nested-loop approach. Classic examples: the "Two Sum"
problem, finding duplicates, grouping anagrams, counting element
frequencies, and checking if two strings are permutations of each
other. Interviewers often look for candidates to recognize *when* a hash
map turns a brute-force solution into an optimal one.

## Advantages

- Average O(1) time for insert, search, and delete
- Extremely versatile — used to solve a huge range of problems
  efficiently (counting, deduplication, fast lookups, grouping)
- Underlies some of the most commonly used built-in data structures
  (`dict`, `set`)

## Disadvantages

- Worst-case performance degrades to O(n) if there are many collisions
- No inherent ordering of elements (though Python's `dict` maintains
  insertion order as an implementation detail since 3.7+)
- Requires a good hash function; a poor one can cause excessive
  collisions and defeat the purpose of hashing
- Resizing (rehashing) a hash table has a cost, though it's typically
  amortized across many operations