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
    index: int = 0
    largest_int: int = input[index]
    while index < len(input):
        if input[index] > largest_int:
            largest_int = input[index]
            index += 1
        else:
            index += 1

    return largest_int
