"""Third challenge question"""

__author__ = "730695410"


def guess_a_number() -> None:
    secret: int = 7
    # below needs to be in the body of the function, otherwise secret is not used
    guessed_number: str = input("Guess a number:")
    print("Your guess was " + guessed_number)
    if int(guessed_number) == secret:  # guessed_number needs to be int
        print("You got it!")
    elif int(guessed_number) < (secret):
        # guessed_number needs to be int, secret can't be str
        # we want to compare values not length of str
        # can't use comparison operator between str and int, need to convert
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
