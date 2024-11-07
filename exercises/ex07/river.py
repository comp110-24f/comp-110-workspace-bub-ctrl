"""File to define River class."""

__author__ = "730695410"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Class for River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks to see which bears and fish survive."""
        surviving_bears: list = []  # establishing empty list
        surviving_fish: list = []  # establishing empty list
        for x in self.fish:  # for each fish in the list
            if x.age <= 3:  # if the age meets survival threshold
                surviving_fish.append(x)  # add the fish to the list of survivors
        for x in self.bears:
            if x.age <= 5:
                surviving_bears.append(x)  # add the bear to the list of survivors
        self.fish = surviving_fish
        self.bears = surviving_bears  # now lists only contain survivors
        return None

    def bears_eating(self):
        """Adjusts values as bears eat."""
        for x in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # syntax to use method in same file
                x.eat(3)  # syntax to use method in different file
        return None

    def remove_fish(self, amount: int):  # new method that removes fish from river
        """Removes fish."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)  # remove fish at first index
            idx += 1
        return None

    def check_hunger(self):
        """Checks to see which bears starve."""
        living_bears: list = []
        for x in self.bears:  # for-in range returns the integer, just use for loop
            if x.hunger_score >= 0:  # if the hunger score of a bear is greater than 0
                living_bears.append(x)  # add that bear to the new list
        self.bears = living_bears  # now the list of bears only contains survivors of the condition
        return None

    def repopulate_fish(self): # incorrect implementation
        new_fish: int = 0
        len(self.fish) = new_fish
        (new_fish//2) * 4 += self.fish
        return None

    def repopulate_bears(self): # incorrect implementation
        new_bears: int = 0
        len(self.bears) = new_bears 
        new_bears//2 += self.bears


        return None

    def view_river(self):  # returns nothing, should print on three different lines
        """Prints the river stats."""
        print(f" ~~~Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week in the river."""
        idx: int = 0
        while idx < 7:  # week has seven days
            self.one_river_day()  # calling method established in same file
            idx += 1
