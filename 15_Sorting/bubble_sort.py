"""
Problem: Write a program to sort a list using bubble sort.
Example:
    Input: [5, 2, 9, 1, 5, 6]
    Output: [1, 2, 5, 5, 6, 9]

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = bubble_sort(numbers)

print(f"Sorted List: {sorted_numbers}")