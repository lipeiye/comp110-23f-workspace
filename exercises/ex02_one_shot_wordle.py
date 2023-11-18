"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730698337"

Secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

Guess_word: str = input('What is your 6-letter guess? ')
Input_len: int = len(Guess_word)
Index_Guess: int = 0
Index_Secret: int = 0
a: int=0
while Input_len != 6:
    Guess_word = input('That was not 6 letters! Try again: ')
    Input_len = len(Guess_word)

while (Index_Guess < 6):
    while (Index_Secret < 6 ):
        if(Guess_word[Index_Guess] == Secret_word[Index_Secret]):
            if(Index_Secret == Index_Guess):
                print (GREEN_BOX, end="")
                if(Index_Guess<5):
                    Index_Guess += 1
                    Index_Secret=0
            elif(Index_Guess != Index_Secret):
                print (YELLOW_BOX, end="")            
                if(Index_Guess<5):
                    Index_Guess += 1
                    if (Index_Guess<5):
                        Index_Secret=0
        if(Guess_word[Index_Guess] != Secret_word[Index_Secret]):
            if(Index_Secret == 5):
                print(WHITE_BOX, end="")
        Index_Secret += 1
    Index_Guess += 1
    Index_Secret = 0




