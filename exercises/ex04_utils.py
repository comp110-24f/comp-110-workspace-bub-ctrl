"""List utility functions!"""

__author__ = "730695410"


def all(list_of_ints: list[int], value: int) -> bool:
    """Checks if all of the ints in the list match the specified value"""
    index: int = 0
    while index < len(list_of_ints):  # loops over the indices to check for matches
        if len(list_of_ints) == 0:
            return False
        if list_of_ints[index] == value:
            index += 1
        else:
            return False  # return False if the indices don't match
    return True  # after every index is checked, if still true return True


def max(input: list[int]) -> int:
    """Returns the largest int in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 1
    largest_int: int = input[0]
    while index < len(input):
        if largest_int > input[index]:  # checks to see if the next number is larger
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
        if (
            int_list_1[index] == int_list_2[index]
        ):  # if they are equal, check the next index
            index += 1
        else:
            return False  # if not equal return False
    return True  # if true at every index return True


def extend(
    int_list_1: list[int], int_list_2: list[int]
) -> None:  # this function does not return anything
    index: int = 0  # local variable because we still need to move through indices
    while index < len(int_list_2):
        int_list_1.append(
            int_list_2[index]
        )  # appends the value at each index to avoid just attaching a list to another
        index += 1  # we don't want a [1, 3, 5, [2, 4, 6]], so append by each index
