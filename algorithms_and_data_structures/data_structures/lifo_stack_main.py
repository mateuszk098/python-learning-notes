"""
LifoStack naive test.
"""

from my_types import lifo_stack as ls


def main():

    s = ls.LifoStack(3, int)
    s.print("Empty: ")

    s.push(1)
    s.push(2)
    s.print("\nAfter push: ")

    print("\nShould be exception:")
    try:
        s.push("abc")
    except Exception as e:
        print(e)

    element = s.pop()
    print("\nPop:", element)

    s.clear()
    s.print("\nAfter clear:")

    print("\nShould be exception:")
    try:
        element = s.pop()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
