"""
Problem: Write a program to sort a list using merge sort.
Example:
    Input: [38, 27, 43, 3, 9, 82, 10]
    Output: [3, 9, 10, 27, 38, 43, 82]

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(left, right)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = merge_sort(numbers)

print(f"Sorted List: {sorted_numbers}")