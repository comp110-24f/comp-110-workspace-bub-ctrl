"""Fifth exercise!"""

__author__ = "730695410"


def only_evens(int_list: list[int]) -> list:
    """A function that returns a list of even ints from an input list."""
    even_list: list[int] = []
    for elem in int_list:
        if elem % 2 == 0:
            even_list.append(elem)
    return even_list


def sub(int_list: list[int], start_index: int, end_index: int) -> list:
    """A function that returns a subset between two indices."""
    sub_list: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(int_list):
        end_index = len(int_list)
    if len(int_list) == 0 or start_index >= len(int_list) or end_index <= 0:
        return sub_list
    for num in range(start_index, end_index):
        sub_list.append(int_list[num])
    return sub_list


def add_at_index(int_list: list[int], added_elem: int, idx: int) -> None:
    if idx < 0 or idx > len(int_list):
        raise IndexError("Index is out of bounds for the input list")
