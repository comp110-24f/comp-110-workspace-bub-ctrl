"""Unit tests for challenge question seven!"""

__author__ = "730695410"

from CQs.cq07.find_max import find_and_remove_max


def test_return_value() -> None:
    """Should return the largest value in the list"""
    example_list: list[int] = [5, 2, 6]
    assert (
        find_and_remove_max(example_list) == 6
    )  # assertion that allows us to test the function


def test_mutate_list() -> None:
    """Should remove largest value from list"""
    example_list: list[int] = [5, 2, 6]
    find_and_remove_max(example_list)
    assert example_list == [5, 2]  # assertion of what the list should look like


def test_edge_case() -> None:
    """Should return -1 when list is empty"""
    assert (
        find_and_remove_max([]) == -1
    )  # assertion testing result of unconventional input
    # empty list should return the value -1 and not mutate the list
