"""
FOUR IN A ROW.
Example from "Beyond the basic stuff with Python" by Al Sweigart.

Description: https://en.wikipedia.org/wiki/Connect_Four
"""

import sys

# Constants used to board display.
EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

# Update BOARD_TEMPLATE and COLUMN_LABELS if you change BOARD_WIDTH
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

BOARD_TEMPLATE = """
    1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+"""


def main():
    """Single game session."""
    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:
        display_board(game_board)
        player_move = get_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        if is_winner(player_turn, game_board):
            display_board(game_board)
            print(f"Player {player_turn} win!")
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)
            print("Draw!")

        # Switch players turn.
        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X


def get_new_board():
    """
    Returns a dict representing the game board.

    The keys are tuple(column_index, row_index) composed of two integers.
    The values are "X", "O" or "." (empty place).
    """
    board = {}
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            board[(column_index, row_index)] = EMPTY_SPACE
    return board


def display_board(board):
    """
    Displays the board and coins on the screen.
    """
    # Prepare a list to pass it to `format()` method in order to display the board.
    # This list contains all coins on the board (from left to right and from bottom to top).
    tile_chars = []
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            tile_chars.append(board[(column_index, row_index)])

    # Display the board.
    print(BOARD_TEMPLATE.format(*tile_chars))


def get_player_move(player_tile, board):
    """
    Permits a player to place his coin in specific column on the board.

    Returns a tuple(column, row) denoting the position of the coin.
    """
    while True:  # Until the player introduces a correct move.
        print(f"Player {player_tile}, enter the number from 1 to {BOARD_WIDTH} or QUIT:")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print(f"Enter the number from 1 to {BOARD_WIDTH}.")
            continue  # Ask the player for a move.

        column_index = int(response) - 1  # -1 because index starts from 0.

        if board[(column_index, 0)] != EMPTY_SPACE:
            print("This column is full. Choose another column.")
            continue  # Ask the player for a move.

        # Find first free field from bottom.
        for row_index in range(BOARD_HEIGHT-1, -1, -1):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return (column_index, row_index)


def is_full(board):
    """Returns True if the board doesn't have empty fields. Otherwise returns False."""
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return False  # Found free field.
    return True  # Every field is taken.


def is_winner(player_tile, board):
    """Returns True if the player sets up "four in a row". Otherwise returns False."""

    # Tranverse the board in order to find "four in a row".
    for column_index in range(BOARD_WIDTH-3):
        for row_index in range(BOARD_HEIGHT):
            # Search for four horizontally, from left to right.
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index+1, row_index)]
            tile3 = board[(column_index+2, row_index)]
            tile4 = board[(column_index+3, row_index)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT-3):
            # Search for four vertically, from top to bottom.
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index, row_index+1)]
            tile3 = board[(column_index, row_index+2)]
            tile4 = board[(column_index, row_index+3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH-3):
        for row_index in range(BOARD_HEIGHT-3):
            # Search for four diagonally, from top to bottom and from left to right.
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index+1, row_index+1)]
            tile3 = board[(column_index+2, row_index+2)]
            tile4 = board[(column_index+3, row_index+3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True
            # Search for four diagonally, from top to bottom and from right to left.
            tile1 = board[(column_index+3, row_index)]
            tile2 = board[(column_index+2, row_index+1)]
            tile3 = board[(column_index+1, row_index+2)]
            tile4 = board[(column_index, row_index+3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    return False


if __name__ == "__main__":
    main()
