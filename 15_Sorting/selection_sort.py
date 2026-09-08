"""
Problem: Write a program to sort a list using selection sort.
Example:
    Input: [64, 25, 12, 22, 11]
    Output: [11, 12, 22, 25, 64]

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def selection_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = selection_sort(numbers)

print(f"Sorted List: {sorted_numbers}")