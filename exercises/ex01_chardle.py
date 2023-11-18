"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730698337"

long_word: str = input("Enter a 5-character word: ")
longword_len: int = len(long_word)

if (longword_len != 5):
    print("Error: Word must contain 5 characters")
    exit()
else:
    target_character: str = input("Enter a single character: ")
    if (len(target_character) != 1):
        print("Error: Character must be a single character.")
        exit()
    else:
        count: int = 0
        index_num: int = 0
        print("Searching for " + target_character + " in " + long_word)
        while index_num < 5:
            if (target_character == long_word[index_num]):
                print(target_character + " found at index " + str(index_num))
                index_num += 1
                count += 1
            else:
                index_num += 1

if (count == 0):
    print("No instances of " + target_character + " found in " + long_word)
if (count > 1):
    print(str(count) + " instances of " + target_character + " found in " + long_word)        
if (count == 1):
    print(str(count) + " instance of " + target_character + " found in " + long_word)   