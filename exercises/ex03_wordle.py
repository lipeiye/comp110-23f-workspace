"""EX03- Structured Wordle."""
__author__ = "730698337"

# Your code will go here 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(long: str, short: str) -> bool:
    """This function check whether the long word contain the short word."""
    assert len(short) == 1
    count: int = 0
    while (count < len(long)):
        if (short == long[count]):
            return True
        else:
            count += 1
    return False


def main() -> None:
    """The entrypoint of the program and main game loop."""
    Try_times: int = 1
    while (Try_times <= 6):
        print("=== Turn " + str(Try_times) + "/6 ===")
        input_guessword: str = input_guess(5)
        wordle_output: str = emojified(input_guessword, "codes")
        print(wordle_output)
        if (wordle_output == GREEN_BOX * 5):
            print("You won in " + str(Try_times) + "/6 turns!")
            return
        Try_times += 1
    if (Try_times > 6):
        print("X/6 - Sorry, try again tomorrow!")


def emojified(guess: str, secret: str) -> str:
    """This function output a series of boxes that work the same as the EX02."""  
    assert len(guess) == len(secret)
    boxes: str = ""
    index_guess: int = 0
    while (index_guess < len(guess)):
        contain: bool = contains_char(secret, guess[index_guess])
        if (guess[index_guess] == secret[index_guess]):
            boxes += GREEN_BOX
        else:
            if (contain):
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX       
        index_guess += 1
    return boxes


def input_guess(len_guess: int) -> str:
    """This function check the input word length."""
    Guess_word = input("Enter a " + str(len_guess) + " character word: ")
    while (len(Guess_word) != len_guess):
        Guess_word = input("That wasn't " + str(len_guess) + " chars! Try again: ")
    return Guess_word


if __name__ == "__main__":
    main()