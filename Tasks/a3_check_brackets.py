from a0_my_stack import Stack


def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

# Использовать Стэк (обьяснял в классе). По очереди проверять каждую скобку и как они закроются, то откидывать их.

    brackets = Stack()
    for i in brackets_row:
        brackets.push(i)
        if len(brackets.stack)
