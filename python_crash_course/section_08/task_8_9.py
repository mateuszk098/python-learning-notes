'''
Passing lists to simple function.
'''


def show_messages(messages: list) -> None:
    '''
    Prints messages in list.
    '''
    for message in messages:
        print(message)


my_mess: list = ['Portuguese Pointer', 'Pudelpointer', 'Korat', 'Asiatic Lion']
show_messages(my_mess)
