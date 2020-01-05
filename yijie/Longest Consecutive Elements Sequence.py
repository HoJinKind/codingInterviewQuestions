# Good morning! Here's your coding interview problem for today.
# This problem was asked by Microsoft.
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4].
# Return its length: 4.
# Your algorithm should run in O(n) complexity.


def longest_consecutive_sequence(arr):
    s = set(arr)
    highest = 0
    counter = 0
    for i in s:
        while i in s:
            counter += 1
            i += 1
        highest = max(highest, counter)
        counter = 0
    return highest


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # 4
print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2, 201, 600, 7, 9, 2000, 8, 10, 11]))  # 5
