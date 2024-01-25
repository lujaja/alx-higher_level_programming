#!/usr/bin/python3
"""
find peak in list of integers
"""

def find_peak(lst):
    """Function to find peak"""
    if not lst:
        return None

    low, high = 0, len(lst) - 1

    while low < high:
        mid = (low + high) // 2
        if lst[mid] > lst[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return lst[low]
