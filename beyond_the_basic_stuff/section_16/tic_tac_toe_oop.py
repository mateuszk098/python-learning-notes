"""
Tic-Tac-Toe - objective version of the game.
Add MiniBoard(TTTBoard) class.
Add HintBoard(TTTBoard) class.
Add HybridBoard(HintBoard, MiniBoard) class.

NOTE:
Both HintBoard and MiniBoard have the method `get_board_str()`.
To figure out why HybridBoard works, we have to look into
MRO - method resolution order and how exactly the `super()` method works. 
When we call the `get_board_str()` method on HybridBoard object, Python will 
know HybridBoard doesn't have this method and checks its parent classes. 
But both parent classes have `get_board_str()` method. Which should be called? 
We can know that by checking the MRO order. To do that, we call `HybridBoard.mro()`. 
The output is as follows:

[<class 'tic_tac_toe_oop.HybridBoard'>, <class 'tic_tac_toe_oop.HintBoard'>, 
<class 'tic_tac_toe_oop.MiniBoard'>, <class 'tic_tac_toe_oop.TTTBoard'>, <class 'object'>]

Let's call the `get_board_str()` method on HybridBoard object. Python will check 
HybridBoard class, HintBoard and MiniBoard then (because we defined inheritance 
from left to right). Finally, Python checks TTTBoard. HintBoard has `get_board_str()`
method, so HybridBoard inherits it, and this method will be called. But it is not
the end. The `get_board_str()` method from HintBoard calls `super()` method. This 
method returns the next class from the MRO list. Therefore, the next method to 
call is `get_board_str()` from MiniBoard class. 

When we change the order in HybridBoard(HintBoard, MiniBoard) to 
HybridBoard(MiniBoard, HintBoard) we lose the hints because the 
`get_board_str()` method from MiniBoard doesn't call `super()` from HintBoard.
"""

import copy
import sys

ALL_SPACES = list("123456789")  # Dictionary keys of the game board.
X, O, BLANK = "X", "O", " "


def main():
    """Single session of the game."""
    print("Hello in the game!")
    if input("Use a mini board? (Y/N): ").lower().startswith("y"):
        game_board = MiniBoard()
    else:
        game_board = HybridBoard()
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


class MiniBoard(TTTBoard):
    def get_board_str(self):
        """Returns text representation of the smaller board."""

        # Replace empty fields with a dot.
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                self._spaces[space] = "."

        s = self._spaces
        board_str = f"""
        {s["1"]}{s["2"]}{s["3"]} 1 2 3
        {s["4"]}{s["5"]}{s["6"]} 4 5 6
        {s["7"]}{s["8"]}{s["9"]} 7 8 9
        """

        # Replace dots with empty field.
        for space in ALL_SPACES:
            if self._spaces[space] == ".":
                self._spaces[space] = BLANK

        return board_str


class HintBoard(TTTBoard):
    def get_board_str(self):
        """Returns text representation of the board with hints."""

        board_str = super().get_board_str()  # Call method from TTTBoard.

        x_can_win = False
        o_can_win = False
        original_spaces = self._spaces

        for space in ALL_SPACES:
            # Simulate X move for this field.
            self._spaces = copy.copy(original_spaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.is_winner(X):
                x_can_win = True
            # Simulate O move for this field.
            self._spaces = copy.copy(original_spaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.is_winner(O):
                o_can_win = True

        if x_can_win:
            board_str += "\nPlayer X can win in the next move."
        if o_can_win:
            board_str += "\nPlayer O can win in the next move."

        self._spaces = original_spaces
        return board_str


class HybridBoard(HintBoard, MiniBoard):
    pass


if __name__ == "__main__":
    main()
