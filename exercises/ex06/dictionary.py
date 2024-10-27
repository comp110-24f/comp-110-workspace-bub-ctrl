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
    for color in input:  # for the color in the list
        if (
            color in count_dictionary
        ):  # if the color is already in the dictionary, add one to value(count)
            count_dictionary[color] += 1
        else:  # if not
            count_dictionary[color] = 1  # set count equal to one
    return count_dictionary


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    new_dict: dict[str, list[str]] = {}  # establish an empty dictionary
    for words in input:  # for the elements in the list
        if words[0].lower() in new_dict:  # if the first letter is in the dictionary
            new_dict[words[0].lower()].append(words)  # add the word at that key
        else:  # if not
            new_dict[words[0].lower()] = [
                words
            ]  # new key with that letter and add the word
    return new_dict


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    if day not in input:  # if the day is not in the dictionary
        input[day] = []  # create an empty list at that key
    if student not in input[day]:  # if the student is not already in that day
        input[day].append(student)  # append the student to the list at that day
