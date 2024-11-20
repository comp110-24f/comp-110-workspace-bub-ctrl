"""Exercise eight!"""

from __future__ import annotations


__author__ = "730695410"


class Node:
    """Defining the Node class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializing Node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)  # .__str__()
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Returns value of Node at index."""
    if head is None:  # index error
        raise IndexError("Index is out of bounds on the list.")

    if index == 0:  # base case
        return head.value
    else:  # recursive case
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns maximum value in the linked list."""
    if head is None:  # value error
        raise ValueError("Cannot call max with None.")

    if head.next is None:  # if only one value in linked list
        return head.value  # that is highest value

    max_value: int = max(head.next)  # recursive call on max_value

    if head.value > max_value:  # if node value is greater than current max
        max_value = head.value  # current max is node value

    return max_value  # ultimately returning an int


def linkify(items: list[int]) -> Node | None:
    """Returns linked list of Nodes with same values."""
    start: int = 0
    end: int = len(items)  # if len(items) == 0:
    if start == end:  # if list is empty, return none
        return None
    else:
        return Node(items[0], linkify(items[1:]))  # splice operator [start:end]


def scale(head: Node | None, factor: int) -> Node | None:
    """Return new linked list of Nodes multiplied by given factor."""
    if head is None:  #
        return None
    return Node(
        head.value * factor, scale(head.next, factor)
    )  # multiplies each value by the given factor
