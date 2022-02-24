def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    # i - 2, j + 1
    # i - 2, j - 1
    # i - 1, j - 2
    # i + 1, j - 2
    #
    # get(i, j) = sum(get(i - 2, j - 1), get(i - 2, j - 1), ...)

    rows = shape[0]   # кол-во строк, отсчет с 1
    cols = shape[1]   # кол-во столбцов, отсчет с 1

    def get_steps(i, j):
        if i == 0 and j == 0:   # левый верхний угол поля
            return 1

        if not 0 <= i < rows:   # выпадаю за границы поля для строк
            return 0
        if not 0 <= j < cols:   # выпадаю за границы поля для столбцов
            return 0

        return sum([get_steps(i - 2, j + 1),
                    get_steps(i - 2, j - 1),
                    get_steps(i - 1, j - 2),
                    get_steps(i + 1, j - 2)])

    return get_steps(i=point[0], j=point[1])


if __name__ == '__main__':
    # Общие тесты не проходят. Он дал только эту проверку.
    assert 13309 == calculate_paths((7, 15), (6, 14))
    assert 2 == calculate_paths((4, 4), (3, 3))
