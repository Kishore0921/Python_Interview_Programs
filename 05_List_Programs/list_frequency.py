"""
Problem: Write a program to find the frequency of each element in a list.
Example:
    Input: [1, 2, 2, 3, 3, 3]
    Output:
        1: 1
        2: 2
        3: 3

Time Complexity: O(n)
Space Complexity: O(k), where k is the number of unique elements
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

for num, count in frequency.items():
    print(f"{num}: {count}")