"""Summing the elements of a list using different loops"""

__author__ = "730695410"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    expression: float = 0.0
    if len(vals) == 0:
        return 0.0
    while index < len(vals):
        expression += vals[index]
        index += 1
    return expression


def f_sum(vals: list[float]) -> float:
    expression: float = 0.0
    if len(vals) == 0:
        return 0.0
    for elem in vals:
        expression += elem
    return expression


def f_range_sum(vals: list[float]) -> float:
    index: int = 0
    expression: float = 0.0
    if len(vals) == 0:
        return 0.0
    for index in range(0, len(vals)):
        expression += vals[index]
    return expression
