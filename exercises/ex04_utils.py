"""List utility functions!"""

__author__ = "730695410"


def all(list_of_ints: list[int], value: int) -> bool:
    """Checks if all of the ints in the list match the specified value"""
    index: int = 0
    while index < len(list_of_ints):
        if list_of_ints[index] == value:
            index += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns the largest int in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 1
    largest_int: int = input[0]
    while index < len(input):
        if largest_int > input[index]:
            index += 1
        else:
            largest_int = input[index]
            index += 1
    return largest_int


def is_equal(int_list_1: list[int], int_list_2: list[int]) -> bool:
    index: int = 0
    if len(int_list_1) != len(int_list_2):
        return False
    while index < len(int_list_1):
        if int_list_1[index] == int_list_2[index]:
            index += 1
        else:
            return False
    return True


def extend(int_list_1: list[int], int_list_2: list[int]) -> None:
    int_list_1.append(int_list_2)
