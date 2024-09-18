def characters(msg: str) -> None:
    index: int = 0
    while index <= len(
        msg
    ):  # bool, if true jump into repeat block (needs to eventually be false)
        print(msg[index])  # line starting repeat block
        index = index + 1  # or index += 1 (this is called relative reassignment)


characters(msg="Howdy")
