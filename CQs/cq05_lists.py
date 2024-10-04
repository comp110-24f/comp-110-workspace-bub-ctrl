"""Mutating functions."""

__author__ = "730695410"


def manual_append(int_list: list[int], value: int) -> None:
    """A function that adds a value to the end"""
    int_list.append(value)  # format for adding a value to a list


def double(int_list: list[int]) -> None:
    """A function that doubles the values in the list"""
    index: int = 0
    while index < len(int_list):
        int_list[index] = int_list[index] * 2  # reassigning a new value to each index
        index += 1  # increasing index by one


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # list_2 to list_1

double(list_2)
print(list_1)
print(list_2)
