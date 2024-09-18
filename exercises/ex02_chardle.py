"""Chardle exercise!"""

__author__: str = "730695410"


def input_word() -> (
    str
):  # defining an input word function with a local variable that takes user input
    """Checks if word followed rules"""
    guessed_word: str = input("Enter a 5-character word: ")
    if len(guessed_word) != 5:
        print("Error: word must contain 5 characters.")
        exit()  # if the input is incorrect, exit instead of returning word
        return guessed_word
    else:
        return guessed_word


def input_letter() -> (
    str
):  # defining an input letter function with a local varible that takes user input
    """Checks if character followed rules"""
    guessed_letter: str = input("Enter a single character: ")
    if len(guessed_letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # exit instead of returning word
        return guessed_letter
    else:
        return guessed_letter


def contains_char(guessed_word: str, guessed_letter: str) -> None:
    """Checks for matching indices"""
    print("Searching for " + guessed_letter + " in " + guessed_word)
    count: int = 0  # loops are more efficient, but a forbidden construct for now
    if guessed_word[0] == guessed_letter:
        print(str(guessed_letter) + " found at index 0")
        count = count + 1
    if guessed_word[1] == guessed_letter:
        print(str(guessed_letter) + " found at index 1")
        count = count + 1
    if guessed_word[2] == guessed_letter:
        print(str(guessed_letter) + " found at index 2")
        count = count + 1
    if guessed_word[3] == guessed_letter:
        print(str(guessed_letter) + " found at index 3")
        count = count + 1
    if guessed_word[4] == guessed_letter:
        print(str(guessed_letter) + " found at index 4")
        count = count + 1
    if count == 0:  # after checking each character
        print(
            "No instances of " + guessed_letter + " found in " + guessed_word
        )  # no matches
    if count == 1:
        print(
            str(count) + " instance of " + guessed_letter + " found in " + guessed_word
        )  # one match
    if count > 1:
        print(
            str(count) + " instances of " + guessed_letter + " found in " + guessed_word
        )  # more than one match


def main() -> None:  # main function that calls our other functions
    contains_char(guessed_word=input_word(), guessed_letter=input_letter())


if __name__ == "__main__":
    main()
