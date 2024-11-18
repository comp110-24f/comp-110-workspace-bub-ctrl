"""Exercise eight!"""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list"""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)  # .__str__()
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    if index == 0:
        return head.value

    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    if head is None:
        raise ValueError("Cannot call max with None.")

    max_value: int = 0

    if head.value > max_value:
        max_value = head.value

    if head.next is None:
        return max_value

    else:
        return max(head.next)


def linkify(items: list[int]) -> Node | None:
    if len(items) == 0:
        return None
    else:
        x: str = str(linkify(items[1 : len(items)]))
        __str__(x)


def scale(head: Node | None, factor: int) -> Node | None:

    return factor * scale(head.value, factor)
