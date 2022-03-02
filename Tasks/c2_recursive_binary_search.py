from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, left_border=None, right_border=None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :param left_border: Левая граница
    :param right_border: Правая граница
    :return: Index of element if it's presented in the arr, None otherwise
    """

    if left_border is None:
        left_border = 0
    if right_border is None:
        right_border = len(arr) - 1

    if left_border > right_border:
        return None

    middle_index = left_border + (right_border - left_border) // 2
    middle_value = arr[middle_index]

    if middle_value == elem:
        return middle_index
    elif middle_value > elem:
        right_border_new = middle_index - 1
        return binary_search(elem, arr, left_border, right_border_new)
    elif middle_value < elem:
        left_border_new = middle_index + 1
        return binary_search(elem, arr, left_border_new, right_border)
