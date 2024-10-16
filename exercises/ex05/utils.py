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
    sub_list: list[int] = []  # this function should not mutate the original
    # instead we add to a new list
    if start_index < 0:  # if negative, start from beginning
        start_index = 0
    if end_index > len(int_list):  # if greater than length, end at end of list
        end_index = len(int_list)
    if len(int_list) == 0 or start_index >= len(int_list) or end_index <= 0:
        return sub_list
    for num in range(start_index, end_index):
        sub_list.append(
            int_list[num]
        )  # appending elements to the new list at that index
    return sub_list


def add_at_index(int_list: list[int], added_elem: int, idx: int) -> None:
    """Shifts list and adds a element at the specified index"""
    if idx < 0 or idx > len(int_list):
        raise IndexError("Index is out of bounds for the input list")  # edge case
    int_list.append(
        1
    )  # this can be any value, it will be reassigned by the int to the left
    for elem in range(
        len(int_list) - 1, idx, -1
    ):  # start at the end of list, stop at index, step left
        # we start at the end of the list and move to the left because we add a value at the end
        int_list[elem] = int_list[elem - 1]
    int_list[idx] = added_elem
