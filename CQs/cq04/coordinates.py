"""Where the coordinates are"""

__author__ = "730695410"


def get_coords(xs: str, ys: str) -> None:
    index_xs: int = 0  # nested while loop that goes over each index
    while index_xs < len(xs):
        index_ys: int = 0  # initializing second index
        while index_ys < len(ys):
            print((xs[index_xs], ys[index_ys]))
            index_ys += 1
        index_xs += 1  # not within the first while loop, index will add 1 before inside while loop
