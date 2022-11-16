"""
Tic-Tac-Toe - functional version of the game.
"""

import sys

ALL_SPACES = list("123456789")  # Dictionary keys of the game board.
X, O, BLANK = "X", "O", " "


def main():
    """Single session of the game."""
    print("Hello in the game!")
    game_board = get_blank_board()
    current_player, next_player = X, O

    while True:
        print(get_board_str(game_board))

        move = None
        while not is_valid_space(game_board, move):
            print("What is your move? (1-9) or QUIT")
            move = input("> ").upper().strip()
            if move == "QUIT":
                sys.exit()
        update_board(game_board, move, current_player)

        # Check if the game is finished.
        if is_winner(game_board, current_player):
            print(get_board_str(game_board))
            print(f"{current_player} won the game!")
            break
        elif is_board_full(game_board):
            print(get_board_str(game_board))
            print("Draw!")
            break

        # Player change.
        current_player, next_player = next_player, current_player

    print("Thank your for the game!")


def get_blank_board():
    """Creates a new empty game board."""
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board


def get_board_str(board):
    """Returns text representation of the board."""
    return f"""
    {board["1"]}|{board["2"]}|{board["3"]} 1 2 3
    -+-+-
    {board["4"]}|{board["5"]}|{board["6"]} 4 5 6
    -+-+-
    {board["7"]}|{board["8"]}|{board["9"]} 7 8 9
    """


def is_valid_space(board, space):
    """Returns True if the board field has correct number and is empty."""
    if space is None:
        return False
    return space in ALL_SPACES and board[space] == BLANK


def is_winner(board, player):
    """Returns True if the player is a winner."""
    b, p = board, player

    # Check if there we have the same characters in a row, col or diagonal.
    return ((b["1"] == b["2"] == b["3"] == p) or  # top row
            (b["4"] == b["5"] == b["6"] == p) or  # middle row
            (b["7"] == b["8"] == b["9"] == p) or  # bottom row
            (b["1"] == b["4"] == b["7"] == p) or  # left col
            (b["2"] == b["5"] == b["8"] == p) or  # middle col
            (b["3"] == b["6"] == b["9"] == p) or  # right col
            (b["1"] == b["5"] == b["9"] == p) or  # first diagonal
            (b["3"] == b["5"] == b["7"] == p))  # second diagonal


def is_board_full(board):
    """Returns True if each field is taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # Found empty field.
    return True


def update_board(board, space, mark):
    """Sets field on the board to a given mark."""
    board[space] = mark


if __name__ == "__main__":
    main()
