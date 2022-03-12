from typing import List


def merge_func(sorted_left: List[int], sorted_right: List[int]):
    sorted_result = []
    current_left_index = 0
    current_right_index = 0

    while True:
        current_left_value = sorted_left[current_left_index]
        current_right_value = sorted_right[current_right_index]

        if current_left_value <= current_right_value:
            # берем значение из левой части
            sorted_result.append(current_left_value)
            current_left_index += 1
        else:
            # берем значение из правой части
            sorted_result.append(current_right_value)
            current_right_index += 1

        if current_left_index == len(sorted_left):
            sorted_result.extend(sorted_right[current_right_index:])
            break
        elif current_right_index == len(sorted_right):
            sorted_result.extend(sorted_left[current_left_index:])
            break

    return sorted_result


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container

    middle_index = len(container) // 2

    left_part = sort(container[:middle_index])
    right_part = sort(container[middle_index:])

    return merge_func(left_part, right_part)
