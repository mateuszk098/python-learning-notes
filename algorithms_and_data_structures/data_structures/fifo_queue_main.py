"""
FifoQueue naive test.
"""

from my_types import fifo_queue as fq


def main():

    q = fq.FifoQueue(3, str)
    q.print("Empty: ")

    q.push("a")
    q.push("b")
    q.print("\nAfter push: ")

    print("\nShould be exception:")
    try:
        q.push(1)
    except Exception as e:
        print(e)

    element = q.pop()
    print("\nFirst Pop:", element)

    element = q.pop()
    print("\nSecond Pop:", element)

    print("\nShould be exception:")
    try:
        element = q.pop()
    except Exception as e:
        print(e)

    shop_queue = fq.FifoQueue(5, str)
    shop_queue.push("Raheem Kunze")
    shop_queue.push("Maida Mueller")
    shop_queue.push("Jaden Kassulke")
    shop_queue.push("Trisha Ortiz")
    shop_queue.push("Zbigniew Json")

    shop_queue.print("\nShop Queue:")

    while not shop_queue.is_empty():
        customer = shop_queue.pop()
        print(customer, "has been served.")

    print("Is shop queue empty?", shop_queue.is_empty())


if __name__ == "__main__":
    main()
