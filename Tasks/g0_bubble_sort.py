from typing import List
from operator import lt, gt   # <, >


def sort(container: List[int], asc: bool = True) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :param asc: Сортировать ли по возрастанию (True) или убыванию (False)
    :return: container sorted in ascending order
    """
    # сортируем по возрастанию
    offset = 1  # смещение относительно конца
    compare_operator = gt if asc else lt

    for _ in range(len(container)):   # O(N)
        is_change = False  # не было замены

        for i in range(len(container) - offset):   # O(N)
            if compare_operator(container[i], container[i + 1]):
                container[i], container[i + 1] = container[i + 1], container[i]
                is_change = True

        if not is_change:   # Если не было изменений, значит список отсортирован
            break
        offset += 1

    return container


if __name__ == '__main__':
    list_ = [-10, 200, 400, 0, -900, -60, 2]
    print(sort(list_))
