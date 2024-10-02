"""Wordle exercise!"""

__author__: str = "730695410"


def input_guess(secret_word_len: int) -> str:
    """A function that takes the guessed word as a input"""
    guessed_word: str = input(f"Enter a {secret_word_len} character word: ")
    while (
        len(guessed_word) != secret_word_len
    ):  # reassigning the local variable so the prompt occurs on the same line in repl
        guessed_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guessed_word


def contains_char(secret_word: str, searched_char: str) -> bool:
    """A function that searches for the character in the word"""
    assert len(searched_char) == 1
    index: int = 0  # so we can search through each character
    while index < len(secret_word):
        if secret_word[index] == searched_char:
            return True  # returning a bool
        index += 1  # if not true then add to index and search again
    return False  # if not true at all then return false


def emojified(guessed_word: str, secret_word: str) -> str:
    """Checks accuracy of guessed_word to secret_word"""
    assert len(guessed_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    final_output: str = ""  # setting an empty string here
    while index < len(guessed_word):
        if guessed_word[index] == secret_word[index]:
            final_output += GREEN_BOX  # add a green box to the empty string
            index += 1  # next index
        elif (
            contains_char(secret_word=secret_word, searched_char=guessed_word[index])
            == True
        ):
            final_output += YELLOW_BOX  # add a green box to the empty string
            index += 1  # next index
        else:
            final_output += WHITE_BOX  # add a white box to the empty string
            index += 1  # next index
    return final_output  # returning the fully concatenated string


def main(secret_word: str) -> None:
    """Program entrypoint and main game loop"""
    turns: int = 1  # one local variable to track the turns
    win: bool = False  # another local variable to track whether the player has won
    while turns < 7 and win == False:
        print(f"=== Turn {turns}/6 ===")  # f string to match the repl
        guess: str = input_guess(
            len(secret_word)
        )  # create a local variable instead of calling the function
        print(
            emojified(guessed_word=guess, secret_word=secret_word)
        )  # that way we avoid duplicate prompts
        if guess == secret_word:
            win = True
        else:
            turns += 1
    if turns == 7:
        print("X/6 - Sorry, try again tomorrow!")
    if win == True:
        print(f"You won in  {turns}/6 turns!")


if __name__ == "__main__":
    main(secret_word="codes")
