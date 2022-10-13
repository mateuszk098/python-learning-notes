'''
While loops and lists.
'''

sandwich_orders: list = ['Cheese', 'Ham', 'Tomato']
finished_sandwich: list = []

while sandwich_orders:
    current_sandwich: str = sandwich_orders.pop()
    print(f"I prepare {current_sandwich}.")
    finished_sandwich.append(current_sandwich)

print(sandwich_orders)
print(finished_sandwich)
