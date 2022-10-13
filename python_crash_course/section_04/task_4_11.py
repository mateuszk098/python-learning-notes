'''
Create list copy.
'''

pizzas: list = ['pepperoni', 'capriciosa', 'americana']
friend_pizzas: list = pizzas[:]  # List copy

pizzas.append('carbonara')
friend_pizzas.append('cheese')

for p in pizzas:
    print(f"My pizza: {p}.")

for fp in friend_pizzas:
    print(f"Friend pizza: {fp}.")

# WITHOUT COPY, BOTH VARIABLES POINTER TO THE SAME LIST!
