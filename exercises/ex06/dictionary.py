"""Exercise six!"""

__author__ = "730695410"


def invert(input: dict[str, str]) -> dict[str, str]:
    inverted_dict: dict[str, str] = (
        {}
    )  # establishing an empty dictionary here to return
    for key in input:
        if input[key] in inverted_dict:  # input[key] is a value
            raise KeyError("Duplicate keys")
        inverted_dict[input[key]] = key  # allows us to swap the keys and values
    return inverted_dict


def favorite_color(input: dict[str, str]) -> str:
    color_dict: dict[str, int] = {}  # establishing an empty dictionary
    most_popular_color: str = ""  # the str that will be returned (most frequent)
    for name in input:  # for the elements in the list
        color = input[name]  # the colors in the dictionary are assigned
        if (
            color not in color_dict
        ):  # if the color encountered is not in dictionary, then
            color_dict[color] = 1  # add a tally of one to the value
        else:
            color_dict[color] += 1  # or add another tally if already in dictionary
    highest_val: int = 0  # int that will be used to compare values in dict
    for (
        colors
    ) in color_dict:  # fix to return the color that appeared in the dictionary first
        if color_dict[colors] > highest_val:  # if value is higher, then
            highest_val = color_dict[colors]  # highest value is now that value
            most_popular_color = (
                colors  # the element with the highest value is now most popular
            )
    return most_popular_color


def count(input: list[str]) -> dict[str, int]:
    count_dictionary: dict[str, int] = {}
    # function that counts the number of times the values appear in the input list
    for color in input:
        if color in count_dictionary:
            count_dictionary[color] += 1
        else:
            count_dictionary[color] = 1
    return count_dictionary


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    new_dict: dict[str, list[str]] = {}
    word_list: list[str] = []
    for words in input:
        word_list.append(words)


# def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
# idx: int = 0
# while idx < len(input):
# input[day] = student
