"""Summing the elements of a list using different loops"""

__author__ = "730695410"


def w_sum(vals: list[float]) -> float:
    """Adds values with a while loop"""
    index: int = 0
    expression: float = 0.0  # a second local variable to track the current sum
    if len(vals) == 0:  # empty list should return zero
        return 0.0
    while index < len(vals):
        expression += vals[index]
        index += 1
    return expression


def f_sum(vals: list[float]) -> float:
    """Adds values with a for... in... loop"""
    expression: float = 0.0
    if len(vals) == 0:
        return 0.0
    for elem in vals:  # for... in... loop
        expression += elem  # doesn't have to be called elem
    return expression


def f_range_sum(vals: list[float]) -> float:
    """Adds values with a for... in range... loop"""
    index: int = 0
    expression: float = 0.0
    if len(vals) == 0:
        return 0.0
    for index in range(0, len(vals)):  # step is automatically set to one
        expression += vals[index]
    return expression
