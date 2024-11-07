"""File to define Fish class."""

__author__ = "730695410"


class Fish:
    """Class for Fish."""

    age: int

    def __init__(self):
        """Initializing Fish with age."""
        self.age = 0
        return None

    def one_day(self):
        """Method for each passing day."""
        self.age += 1  # age should increase by one per day
        return None
