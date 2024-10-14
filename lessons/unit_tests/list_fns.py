"""In-class list functions."""

__author__ = "730695410"


# get_first: takes a list[str] as input and returns first element
def get_first(input: list[str]) -> str:
    """Return first element"""
    return input[0]


# remove_first: takes a list[str] as input and removes first element (returns nothing)
def remove_first(input: list[str]) -> None:
    """Remove first element"""
    input.pop(0)


# get_and_remove_first: takes a list[str] as input and returns + removes first element
def get_and_remove_first(input: list[str]) -> str:
    """Remove and return first element"""
    first_element: str = input[0]
    input.pop(0)
    return first_element
