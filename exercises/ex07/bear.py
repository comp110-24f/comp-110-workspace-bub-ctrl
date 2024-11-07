"""File to define Bear class."""

__author__ = "730695410"


class Bear:
    """Class for Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing Bear with age and hunger."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Method for each passing day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Method for changing hunger score by fish."""
        self.hunger_score += num_fish  # one fish = one hunger_score
        return None
