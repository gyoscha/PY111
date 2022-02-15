"""
Taylor series
"""
import math
from typing import Union
from itertools import count

EPSILON = 0.0001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    def get_item_n(n):
        return x ** n / math.factorial(n)

    sum_ = 1
    for i in count(1, 1):
        current_item = get_item_n(i)
        sum_ += current_item
        if current_item <= EPSILON:
            break

    return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    def get_item_n(n):
        return (-1) ** (n - 1) * x ** (2 * n - 1) / math.factorial(2 * n - 1)

    sum_ = 0
    for i in count(1, 1):
        current_item = get_item_n(i)
        sum_ += current_item
        if abs(current_item) <= EPSILON:
            break

    return sum_
