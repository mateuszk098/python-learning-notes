'''
Who Wants to Be a Millionaire? Simple console game.
'''

import json
import random

points: int = 0
game: bool = True
money: list[int] = [0, 500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000,
                    250000, 500000, 1000000]


def show_question(question) -> None:
    global points
    global game

    print()
    print(question["question"])
    print()
    print("A:", question["A"])
    print("B:", question["B"])
    print("C:", question["C"])
    print("D:", question["D"])
    print()

    # Answer validation
    while True:
        answer: str = input("Which answer do you choose? ")
        if answer not in ("A", "B", "C", "D"):
            print("Please choose A, B, C or D. ")
            print()
        else:
            break

    # Answer correctness validation.
    if answer == question["answer"]:
        points += 1
        print("Correct answer! You have", money[points], "PLN.")

        while True:
            if points == 12:
                print()
                print("End of game. You win", money[points], "PLN.")
                break
            else:
                print()
                play_more: str = input("Do you want to continue game? ")
                if play_more not in ("Yes", "No"):
                    print("Please choose Yes or No. ")
                elif play_more == "No":
                    game = False
                    print()
                    print("End of game. You win", money[points], "PLN.")
                    break
                else:
                    break

    else:
        print("Wrong answer! Correct answer is:", question["answer"])
        print()
        if points < 2:
            print("End of game. You win", money[0], "PLN.")
        if points >= 2 and points < 7:
            print("End of game. You win", money[2], "PLN.")
        elif points >= 7:
            print("End of game. You win", money[7], "PLN.")
        game = False


with open("millionaire_game_qa.json") as json_file:
    questions = json.load(json_file)
    random.shuffle(questions)

for i in range(0, 12):
    show_question(questions[i])
    if game == False:
        break
