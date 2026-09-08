"""
Problem: Write a program to sort a list using insertion sort.
Example:
    Input: [12, 11, 13, 5, 6]
    Output: [5, 6, 11, 12, 13]

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = insertion_sort(numbers)

print(f"Sorted List: {sorted_numbers}")