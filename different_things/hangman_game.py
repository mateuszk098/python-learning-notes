"""
Hangman. Simple game in the console.
"""

import sys


def find_indexes(word: str, letter: str) -> list[int]:
    """ Looking for indices of used letter. """

    indexes: list[int] = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def state_of_game(no_of_tries: int, used_letters: list[str], user_word) -> None:
    print()
    print(" ".join(user_word))
    print("No. of tries: ", no_of_tries)
    print("Used letters.: ", used_letters)
    print()


def level_choice() -> int:
    print()
    while True:
        level: str = input("Difficulty: [1] - Easy [2] - Medium [3] - Hard: ")
        if level == "1":
            no_of_tries: int = 5
            break
        elif level == "2":
            no_of_tries = 3
            break
        elif level == "3":
            no_of_tries = 1
            break
        else:
            print("Incorrect value.")

    print("No. of tries:", no_of_tries)
    print()
    return no_of_tries


def game(word: str, no_of_tries: int) -> None:

    used_letters: list[str] = []
    user_word: list[str] = ["_" for _ in word]

    while True:
        letter: str = input("Enter one letter: ")
        used_letters.append(letter)

        # Indices of given letter if it is in the guessed word.
        found_idexes: list[int] = find_indexes(word, letter)

        if not found_idexes:
            print("There is not this letter.!")
            no_of_tries -= 1

            if no_of_tries == 0:
                print("You lose!!")
                break
        else:
            for index in found_idexes:
                user_word[index] = letter

            if "".join(user_word) == word:
                print()
                print("Congratulations! You have successfully guessed the answer.")
                break

        state_of_game(no_of_tries, used_letters, user_word)

    print("Your score: ")
    state_of_game(no_of_tries, used_letters, user_word)

    used_letters.clear()
    user_word.clear()


if __name__ == "__main__":
    word: str = "Natalia"
    while True:
        no_of_tries: int = level_choice()
        game(word, no_of_tries)

        play: str = input("Do you want to play one more time? ")
        if play == "Y":
            continue
        elif play == "N":
            print("End!")
            sys.exit(0)
        else:
            print("Error value!")
