"""Fourth challenge question!"""

__author__ = "730695410"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # local variable for count
    index: int = 0  # local variable for index
    while index < len(phrase):
        if (
            phrase[index] == search_char
        ):  # if the index of the phrase matches the character...
            count = count + 1  # assign count a new value, count + 1
        index = (
            index + 1
        )  # index should increase by one, so we can evaluate the next character
    return count  # return the count
