import random
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    # not inplace
    # if not container:
    #     return container
    #
    # mid = container[len(container) // 2 - 1]   # можно выбрать как угодно!
    #
    # left_part = [value for value in container if value < mid]
    # right_part = [value for value in container if value > mid]
    #
    # middle_part = [value for value in container if value == mid]
    #
    # return sort(left_part) + middle_part + sort(right_part)

    # inplace
    def _sort(left_border, right_border) -> None:
        # left_border и right_border - это индексы.
        if left_border >= right_border:   # базовый случай
            return None

        random_index = random.randint(left_border, right_border)
        pivot = container[random_index]
        # слайсирование создает копию всегда

        i, j = left_border, right_border

        while i <= j:
            while container[i] < pivot:
                i += 1

            while container[j] > pivot:
                j -= 1

            if i <= j:
                container[i], container[j] = container[j], container[i]
                i += 1
                j -= 1

        _sort(left_border, j)
        _sort(i, right_border)

    _sort(0, len(container) - 1)
    return container
