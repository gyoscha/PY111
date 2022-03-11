from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    # сортируем по возрастанию
    offset = 1  # смещение относительно конца

    for _ in range(len(container)):   # O(N)
        is_change = False  # не было замены

        for i in range(len(container) - offset):   # O(N)
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                is_change = True

        if not is_change:   # Если не было изменений, значит список отсортирован
            break
        offset += 1

    return container


if __name__ == '__main__':
    list_ = [-10, 200, 400, 0, -900, -60, 2]
    print(sort(list_))
