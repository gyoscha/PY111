from typing import Union, Sequence
# from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    total_costs = {}

    # @lru_cache(maxsize=None)
    def lazy_stairway_path(stair_number: int) -> Union[float, int]:
        """Принимает номер ступени, возвращает стоимость"""
        if stair_number in total_costs:   # мемоизация
            return total_costs[stair_number]   # не считать, а сразу вернуть результат

        if stair_number == 0:
            total_costs[stair_number] = stairway[stair_number]
            return total_costs[stair_number]
        if stair_number == 1:
            total_costs[stair_number] = stairway[stair_number]
            return total_costs[stair_number]

        current_cost = stairway[stair_number]

        total_costs[stair_number] = current_cost + min(lazy_stairway_path(stair_number-1),
                                                       lazy_stairway_path(stair_number-2))
        return total_costs[stair_number]

    return lazy_stairway_path(len(stairway) - 1)


def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    ...
    # stairway - цена ступени
    count_stairs = len(stairway)   # количество ступеней
    total_cost = [0] * count_stairs   # стоимости дойти до ступеней

    # изначальные условия для 1 и 2 ступени
    total_cost[0] = stairway[0]
    # total_cost[1] = stairway[1]
    total_cost[1] = min(stairway[1], stairway[0] + stairway[1])

    # прямой метод обхода (i-стоимость = i-цена + min((i - 1)-стоимость, (i - 2)-стоимость))
    for i in range(2, count_stairs):
        total_cost[i] = stairway[i] + min(total_cost[i - 1], total_cost[i - 2])

    return total_cost[-1]


def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    # stairway - цена ступени
    count_stairs = len(stairway)  # количество ступеней
    total_cost = [float('inf')] * count_stairs  # стоимости дойти до ступеней

    # изначальные условия для 1 и 2 ступени
    total_cost[0] = stairway[0]
    total_cost[1] = min(stairway[1], stairway[0] + stairway[1])

    # Обратный метод
    # for i in range(0, count_stairs):
    #     if i + 1 < count_stairs:
    #         total_cost[i + 1] = min(stairway[i + 1] + total_cost[i], total_cost[i + 1])
    #
    #     if i + 2 < count_stairs:
    #         total_cost[i + 2] = min(stairway[i + 2] + total_cost[i], total_cost[i + 2])

    for i in range(0, count_stairs - 2):
        total_cost[i + 1] = min(stairway[i + 1] + total_cost[i], total_cost[i + 1])
        total_cost[i + 2] = min(stairway[i + 2] + total_cost[i], total_cost[i + 2])

    total_cost[-1] = min(stairway[-1] + total_cost[-2], total_cost[-1])
    return total_cost[-1]
