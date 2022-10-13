'''
Passing lists to simple function.
'''


def send_messages(messages: list, send_messages: list) -> None:
    '''
    Prints and pass messages to antoher list
    '''
    while messages:
        message: str = messages.pop()
        print(f"I pass {message} to send_messages.")
        send_messages.append(message)


my_mess: list = ['Portuguese Pointer', 'Pudelpointer', 'Korat', 'Asiatic Lion']
send_mess: list = []

send_messages(my_mess, send_mess)
print(my_mess)
print(send_mess)
