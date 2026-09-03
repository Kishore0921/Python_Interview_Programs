"""
Problem: Write a program to count the frequency of each word in a
sentence using a dictionary.
Example:
    Input: "the quick brown fox the fox"
    Output:
        the: 2
        quick: 1
        brown: 1
        fox: 2

Time Complexity: O(n)
Space Complexity: O(k), where k is the number of unique words
"""

text = input("Enter a sentence: ")
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(f"{word}: {count}")