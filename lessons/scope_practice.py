"""Global variables and scope practice"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # set up empty string and then we can copy values over
    index: int = 0  # local variables: copy, index, msg, and char
    # print(word) this works because global variables can be accessed inside functions
    while index < len(msg):
        # if the letter is NOT char
        if msg[index] != char:
            # add it to copy
            copy = copy + msg[index]
            # we could also write it as copy += msg[index]
        index = index + 1  # we could also write it as index += 1
    return copy


if __name__ == "__main__":
    # create a variable called word with the value yoyo
    word: str = "yoyo"  # same syntax, different scope: global variable
    # print the result of calling your function with arguments word and "y"
    print(remove_chars(word, "y"))  # positional argument
# print the result of calling your function with arguments word and "o"
# print(remove_chars(word, "o"))  # positional argument

# print(copy) wouldn't work because local variables can't be accessed outside function
