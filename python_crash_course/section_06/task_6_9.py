'''
Embedd lists in dictionary.
'''

favorite_places: dict = {'Kacie': ['Madrid', 'San Francisco'],
                         'Jordy': ['Barcelona', 'Venezia', 'Paris'],
                         'Jeffrey': ['Bucharest', 'Warsaw']}

for person, places in favorite_places.items():
    print(f"{person} favourite places are:")
    for place in places:
        print(place, end=' ')
    print('\n')
