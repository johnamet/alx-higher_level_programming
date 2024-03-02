#!/usr/bin/python3
"""
Finds the peak in an unsorted list of integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
            list_of_integers: A list of unsorted integers.

    Returns:
            An integer representing a
            peak in the list. If there are multiple peaks,
            any one of them may be returned.
    """

    # Handle base cases

    if len(list_of_integers) is None or list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    # Recursively search for the peak
    # in the left and right halves of the list

    mid_index = len(list_of_integers) // 2
    left_peak = find_peak(list_of_integers[:mid_index])
    right_peak = find_peak(list_of_integers[mid_index:])

    # Compare the peak candidates and return the largest one
    return max(left_peak, right_peak)
