"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_elem = arr[0]
    min_index = 0
    for index, value in enumerate(arr):
        if value < min_elem:
            min_elem = value
            min_index = index
    return min_index


if __name__ == '__main__':
    arr = [1, 5, 10, -7]
    print(min_search(arr))
