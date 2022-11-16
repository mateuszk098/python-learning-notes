"""
Tic-Tac-Toe - objective version of the game.
"""

import sys

ALL_SPACES = list("123456789")  # Dictionary keys of the game board.
X, O, BLANK = "X", "O", " "


def main():
    """Single session of the game."""
    print("Hello in the game!")
    game_board = TTTBoard()
    current_player, next_player = X, O

    while True:
        print(game_board.get_board_str())

        move = None
        while not game_board.is_valid_space(move):
            print("What is your move? (1-9) or QUIT")
            move = input("> ").upper().strip()
            if move == "QUIT":
                sys.exit()
        game_board.update_board(move, current_player)

        # Check if the game is finished.
        if game_board.is_winner(current_player):
            print(game_board.get_board_str())
            print(f"{current_player} won the game!")
            break
        elif game_board.is_board_full():
            print(game_board.get_board_str())
            print("Draw!")
            break

        # Player change.
        current_player, next_player = next_player, current_player

    print("Thank your for the game!")


class TTTBoard:
    """Tic-tac-toe game board class."""

    def __init__(self, use_pretty_board=False, use_logging=False):
        """Creates a new empty game board."""
        self._spaces = {}
        for space in ALL_SPACES:
            self._spaces[space] = BLANK

    def get_board_str(self):
        """Returns text representation of the board."""
        s = self._spaces
        return f"""
        {s["1"]}|{s["2"]}|{s["3"]} 1 2 3
        -+-+-
        {s["4"]}|{s["5"]}|{s["6"]} 4 5 6
        -+-+-
        {s["7"]}|{s["8"]}|{s["9"]} 7 8 9
        """

    def is_valid_space(self, space):
        """Returns True if the board field has correct number and is empty."""
        if space is None:
            return False
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def is_winner(self, player):
        """Returns True if the player is a winner."""
        s, p = self._spaces, player

        # Check if there we have the same characters in a row, col or diagonal.
        return ((s["1"] == s["2"] == s["3"] == p) or  # top row
                (s["4"] == s["5"] == s["6"] == p) or  # middle row
                (s["7"] == s["8"] == s["9"] == p) or  # bottom row
                (s["1"] == s["4"] == s["7"] == p) or  # left col
                (s["2"] == s["5"] == s["8"] == p) or  # middle col
                (s["3"] == s["6"] == s["9"] == p) or  # right col
                (s["1"] == s["5"] == s["9"] == p) or  # first diagonal
                (s["3"] == s["5"] == s["7"] == p))  # second diagonal

    def is_board_full(self):
        """Returns True if each field is taken."""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # Found empty field.
        return True

    def update_board(self, space, mark):
        """Sets field on the board to a given mark."""
        self._spaces[space] = mark


if __name__ == "__main__":
    main()
