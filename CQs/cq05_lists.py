"""Mutating functions"""

__author__ = "730695410"


def manual_append(int_list: list[int], value: int) -> None:
    int_list.append(value)


def double(int_list: list[int]) -> None:
    index: int = 0
    while index < len(int_list):
        int_list[index] = int_list[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
