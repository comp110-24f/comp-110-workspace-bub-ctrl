"""Global variables and scope practice"""


def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if msg[index] == char:
            index = index + 1

    return copy
