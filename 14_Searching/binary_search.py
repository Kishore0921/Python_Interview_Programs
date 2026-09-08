"""
Problem: Write a program to search for an element in a sorted list
using binary search.
Example:
    Input: [1, 3, 5, 7, 9, 11], target = 7
    Output: Element found at index 3

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


numbers = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the number to search for: "))

result = binary_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")