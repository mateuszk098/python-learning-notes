'''
While loops and lists.
'''

sandwich_orders: list = ['Cheese', 'Ham', 'Pastrami', 'Tomato', 'Pastrami']
finished_sandwich: list = []

print(sandwich_orders)
print(finished_sandwich)

lack_sandwich: str = 'Pastrami'
print(f"We currently don't have {lack_sandwich}.")

while sandwich_orders:
    current_sandwich: str = sandwich_orders.pop()

    if current_sandwich == 'Pastrami':
        while current_sandwich in sandwich_orders:
            sandwich_orders.remove(current_sandwich)
    else:
        print(f"I prepare {current_sandwich}.")
        finished_sandwich.append(current_sandwich)

print(sandwich_orders)
print(finished_sandwich)
