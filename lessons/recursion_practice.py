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


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: None | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


# print(to_str(one))
# print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # base case: when head is the last node, return its value
    # print(f"Enter last ({head.value})")
    if head.next is None:
        # print(f"Return base case: {head.value}")
        return head.value
    # recursive case: figure out the last node (recursive call) in rest of list
    # return its value
    else:
        rest: int = last(head.next)
        # print(f"Return recursive case: {head.value} -> {rest}")
        return rest

    return -1


print(last(one))  # expect to print 2
print(last(courses))  # expect to print 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end."""
    
    # can you handle an edge case, if so raise ValueError("invalid arguments")
    if start > end:
        raise ValueError("Invalid arguments, start > end")
    if start == end:  # base case
        return None
    else:  # recursive case
        # 1. first handle the first value in new list here
        # first: int = start
        # return Node(first, recursive_range(start + 1, end))
        # 2. let rest of the list be handled recursively
        # rest: Node | None = recursive_range(start + 1, end)
        # all on one line: return Node(start, recursive_range(start + 1, end))


    a_list: Node | None = recursive_range(110, 113)
    print(a_list)