"""Tests for fifth exercise"""

__author__ = "730695410"

from exercises.ex05.utils import (
    only_evens,
    sub,
    add_at_index,
)  # condensed to avoid redundancy


import pytest  # necessary so that the index error can be raised properly for

# add_at_index edge case

# only_evens unit tests below


def test_only_evens_rv() -> None:
    """Tests that the returned list has only even ints"""
    example_list: list[int] = [1, 3, 4, 6]
    assert (only_evens(example_list)) == [4, 6]


def test_only_evens_behavior() -> None:
    """Tests that the input list is not modified by only_evens"""
    example_list: list[int] = [9, 10, 2, 5]
    only_evens(
        example_list
    )  # calling the function first then making the assertion will check
    assert example_list == [9, 10, 2, 5]  # since we already checked the return value


def test_only_evens_edge_case() -> None:
    """Tests that only evens function returns empty list if no ints are even"""
    example_list: list[int] = [1, 3, 5]
    assert (
        only_evens(example_list)
    ) == []  # should return empty list if no ints are even


# sub unit tests below


def test_sub_rv() -> None:
    """Tests that the returned list contains the proper subset"""
    example_list: list[int] = [4, 5, 8, 2, 5]
    assert (sub(example_list, 2, 4)) == [8, 2]  # end index is itself -1


def test_sub_behavior() -> None:
    """Tests that input list is not modified by sub"""
    example_list: list[int] = [4, 5, 8, 2, 5]
    sub(example_list, 1, 4)
    assert example_list == [4, 5, 8, 2, 5]


def test_sub_edge_case() -> None:
    """Tests that sub returns empty list if input list is empty"""
    example_list: list[int] = []
    assert (
        sub(example_list, 2, 5)
    ) == []  # indices here don't really matter, len(example_list) == 0


# add_at_index unit tests below


def test_add_at_index_rv() -> None:
    """Tests that function add_at_index does not return anything"""
    # because add_at_index in utils.py returns None
    example_list: list[int] = [2, 4, 6]
    assert (add_at_index(example_list, 5, 2)) == None  # syntax works for now


def test_add_at_index_behavior() -> None:
    """Tests that input list is modified by add_at_index"""  # list SHOULD be mutated
    example_list: list[int] = [5, 10, 15]
    add_at_index(example_list, 2, 0)
    assert example_list == [2, 5, 10, 15]


def test_index_error() -> None:
    """Tests that index error is raised for invalid index"""
    test_list: list[int] = [1, 2, 3]
    with pytest.raises(
        IndexError
    ):  # because the exceptions aren't returned, we raise via pytest
        add_at_index(test_list, 2, 5)
