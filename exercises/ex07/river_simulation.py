"""Simulating the river."""

__author__ = "730695410"

from ex07.river import River


class River:  # can the name of the river change here?

    def __init__(self) -> None:
        self.fish = 10
        self.bear = 2

    def view_river(self) -> None:
        x: int = 0  # current day of the river
        y: int = self.fish  # number of fish in the river
        z: int = self.bear  # number of bears in the river
        print(f"~~~ Day {x:} ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")


my_river.view_river()  # "No module named 'ex07"
