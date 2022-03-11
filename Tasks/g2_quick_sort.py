from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if not container:
        return container

    mid = container[len(container) // 2 - 1]   # можно выбрать как угодно!

    left_part = [value for value in container if value < mid]
    right_part = [value for value in container if value > mid]

    middle_part = [value for value in container if value == mid]

    return sort(left_part) + middle_part + sort(right_part)
