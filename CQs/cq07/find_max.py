"""Challenge question seven!"""

__author__ = "730695410"


def find_and_remove_max(
    int_list: list[int],
) -> int:  # a function that returns the largest value
    if len(int_list) == 0:  # edge case
        return -1
    index: int = 0
    max_int: int = int_list[0]
    index2: int = (
        0  # second index to use in while loop that removes max value from list
    )

    while index < len(int_list):
        if max_int > int_list[index]:
            index += 1
        else:
            max_int = int_list[index]
            index += 1
    while index2 < len(int_list):
        if max_int == int_list[index2]:
            int_list.pop(index2)  # index of largest value until if becomes false
        else:
            index2 += 1
    return max_int  # returning an int, not the new list
