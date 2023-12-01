#!/usr/bin/env python3

"""
finds the peak in a given list of unsorted integers
"""

def find_peak(array):
    """
    Finds a peak element in a list.

    Args:
        array (list): The input list.

    Returns:
        int or None: The peak element if found, otherwise None.
    """
    n = len(array)
    if n == 0:
        return None
    if n == 1:
        return array[0]

    start, end = 0, n - 1

    while start < end:
        mid = (start + end) // 2

        if array[mid] > array[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return array[start]

# Uncomment the lines below for testing with command-line arguments
# if __name__ == "__main__":
#     import sys
#     args = sys.argv[1:]
#     numbers = [int(arg) for arg in args]
#     print(find_peak(numbers))
