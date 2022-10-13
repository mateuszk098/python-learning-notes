'''
Simple function with dictionary. User complete info.
'''


def make_album(band: str, album: str, songs=None) -> dict:
    '''
    Returns dictionary with album information.
    '''

    info: dict = {'Band': band, 'Album': album}

    if songs is not None:
        info['Songs'] = songs

    return info


while True:
    my_band: str = input('Enter your favourite band: ')
    my_album: str = input('Enter your favourite album: ')

    my_dict: dict = make_album(my_band, my_album)
    print(my_dict)

    end: str = input("Enter 'quit' to exit: ")
    if end == 'quit':
        break
