#!/usr/bin/python3
"""
Find peak module
"""


def find_peak(list_of_integers):
    """
    Finds the peak(highest value) in a given array of integers
    Args:
        list_of_integers: array of type number
    Return:
        the highest integer from the array(peak)
    """
    peak = None
    len_l = len(list_of_integers)
    if len_l < 3:
        return None
    for idx in range(1, len_l - 1):
        left = list_of_integers[idx - 1]
        mid = list_of_integers[idx]
        right = list_of_integers[idx + 1]
        if (left <= mid) and (mid >= right):
            peak = mid
    return peak
