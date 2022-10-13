'''
Simple function with dictionary.
'''


def make_album(band: str, album: str, songs=None) -> dict:
    '''
    Returns dictionary with album information.
    '''

    info: dict = {'Band': band, 'Album': album}

    if songs is not None:
        info['Songs'] = songs

    return info


my_album_1: dict = make_album('Linkin Park', 'Meteora')
my_album_2: dict = make_album('Linkin Park', 'Hybrid Theory', 8)

print(my_album_1)
print(my_album_2)
