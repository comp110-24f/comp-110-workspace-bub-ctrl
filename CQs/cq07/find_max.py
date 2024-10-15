"""Challenge question seven!"""

__author__ = "730695410"


def find_and_remove_max(int_list: list[int]) -> int:
    if len(int_list) == 0:
        return -1
    index: int = 0
    max_int: int = int_list[0]
    while index < len(int_list):
        if max_int > int_list[index]:
            index += 1
        else:
            max_int = int_list[index]
            index += 1
    int_list.pop(index - 1)
    return max_int
