from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    # первый символ всегда 0, поэтому заносим и пропускаем
    p = [0] * len(prefix_str)
    for i in range(1, len(prefix_str)):
        k = p[i - 1]
        while k > 0 and prefix_str[i] != prefix_str[k]:
            k = 0
        if prefix_str[i] == prefix_str[k]:
            k += 1
        p[i] = k
    return p


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """

    ii = 0   # Счетчик ii = 0, который «смотрит» на строку
    j = 0   # Счетчик j = 0, который «смотрит» на шаблон
    pi = _prefix_fun(substr)   # Префикс таблица pi, построенная по шаблону

    while ii < len(inp_string):
        current_str = inp_string[ii]
        current_sub = substr[j]

        if current_sub == current_str:
            ii += 1
            j += 1

            if j == len(substr):
                return ii - len(substr)   # условие выхода (индекс элемента с которого началось вхождение шаблона)

        elif j > 0:
            j = pi[j - 1]
        else:
            ii += 1

    return None


