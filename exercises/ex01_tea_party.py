"""Tea party details!"""

__author__: str = "730695410"


# defining the main function here
# return type is none, so we don't need the return keyword in the body
def main_planner(guests: int) -> None:
    """Number of people coming, tea bags, treats, and total cost."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    # we want the cost, and have to fill in the arguments here


# defining the tea_bags function here
def tea_bags(people: int) -> int:
    """The number of tea bags needed for the party."""
    return people * 2


# above we want the number of tea bags to be double the number of people


# defining the treats function here
def treats(people: int) -> int:
    """The number of treats needed for the party."""
    return int((tea_bags(people=people)) * 1.5)


# defining the cost function here
def cost(tea_count: int, treat_count: int) -> float:
    """The total cost of the party."""
    return (tea_count * 0.50) + (treat_count * 0.75)


# cost of tea plus cost of treats = total cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
