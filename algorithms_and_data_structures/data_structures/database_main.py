"""
DataBase naive test.
"""

from my_types import database as db


def main():
    base = db.DataBase()

    base.add_and_sort("Franecki", 5000)
    base.add_and_sort("Hand", 6500)
    base.add_and_sort("Emmerich", 8000)
    base.add_and_sort("Gulgowski", 2500)

    print("Unsorted:")
    base.print_out()
    print("\nSorted by name:")
    base.print_out_by_name()
    print("\nSorted by salary:")
    base.print_out_by_salary()

    base.remove_person("Emmerich")
    base.remove_person("Hand")

    print("\nAfter remove 'Emmerich' and 'Hand':\n")
    print("Unsorted:")
    base.print_out()
    print("\nSorted by name:")
    base.print_out_by_name()
    print("\nSorted by salary:")
    base.print_out_by_salary()


if __name__ == "__main__":
    main()
