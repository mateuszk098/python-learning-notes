"""
TOWER OF HANOI.
Example from "Beyond the basic stuff with Python" by Al Sweigart.
"""

import sys
import copy

TOTAL_DISKS = 5  # More - harder.
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))  # All disks are on the A tower.


def main() -> None:
    """Single game session."""

    """
    The towers dictionary contains "A", "B" and "C" keys and values, which are lists representing
    disks towers. Single tower contains integers representing disks with different width,
    where the index 0 of the list means tower base. In the case of 5 disks, the tower 
    [5, 4, 3, 2, 1] represents a complete tower. Empty list [] represents a empty tower.
    In the [1, 3] list, a bigger disk is placed on the smaller one, and it is invalid placement.
    In the [3, 1] list, a smaller disk is placed on the bigger one, and it is a proper placement.
    """
    towers: dict[str, list[int]] = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:  # One move in one iteration.
        display_towers(towers)

        from_tower, to_tower = get_player_move(towers)
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        if SOLVED_TOWER in (towers["B"], towers["C"]):
            display_towers(towers)
            print("You solved the Tower of Hanoi problem!")
            sys.exit()


def get_player_move(towers):
    """Asks the player for a move. Returns from_tower, to_tower."""

    while True:  # Ask until the player enters a proper move.
        print("Enter letters for tower 'from' and 'to' or 'QUIT'.")
        print("(e.g. enter AB in order to move disk from tower A to B.)\n")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thnak you for the game!")
            sys.exit()

        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of the combinations AB, AC, BA, BC, CA, CB")
            continue  # Ask the player for a move.

        from_tower, to_tower = response

        if not towers[from_tower]:
            print("Tower 'from' cannot be empty!")
            continue  # Ask the player for a move.
        elif not towers[to_tower]:
            return from_tower, to_tower  # This is a proper move.
        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print("You cannot place a bigger disk on a smaller!")
            continue  # Ask the player for a move.
        else:
            return from_tower, to_tower  # This is a proper move.


def display_towers(towers):
    """Displays 3 towers within their disks."""

    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)  # Empty bar without disks.
            else:
                display_disk(tower[level])
        print()

    # Print towers labels.
    empty_space = " " * TOTAL_DISKS
    print("{0} A{0}{0} B{0}{0} C\n".format(empty_space))


def display_disk(width):
    """Displays a disk within the certain width. Width 0 means lack of disk."""

    empty_space = " " * (TOTAL_DISKS - width)

    if width == 0:
        print(f"{empty_space}||{empty_space}", end="")
    else:
        disk = "#" * width
        num_label = str(width).rjust(2, "_")
        print(f"{empty_space}{disk}{num_label}{disk}{empty_space}", end="")


if __name__ == "__main__":
    main()
