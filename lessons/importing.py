from lessons.scope_practice import remove_chars

"""Practice importing."""

__author__ = "730695410"


# when we import a file, python will take and run the entire file

from lessons.scope_practice import word

# if you are importing multiple things from the same file use a comma
# ex: from lessons.scope_practice import remove_chars, word

# only works if __main__ is in the file you are pulling from
print(remove_chars("happy", "p"))
