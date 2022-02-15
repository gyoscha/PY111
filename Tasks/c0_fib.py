from typing import Iterable


def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm
    n >= 0
    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:   # O(n)
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm
    n >= 0
    :param n: number of item
    :return: Fibonacci number
    """
    # Возвращает n-е число
    if n < 0:
        raise ValueError

    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b


def generator_fib(n: int) -> Iterable:
    # Возвращает первые n чисел
    if n < 0:
        raise ValueError

    a = 0
    yield a
    b = 1
    yield b

    for _ in range(n - 1):
        a, b = b, a + b
        yield b


if __name__ == '__main__':
    N = 10
    list_fib = [fib_iterative(i) for i in range(N)]   # Сложность O(n ** 2)

    print(list_fib)

    # через генератор
    list_gen_fib = [num for num in generator_fib(N - 1)]  # Сложность O(n)
    print(list_gen_fib)
