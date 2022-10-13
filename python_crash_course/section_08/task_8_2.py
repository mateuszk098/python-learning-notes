'''
Simple fuction with parameter.
'''


def display_message(message_to_disp: str) -> None:
    '''
    Prints simple message.
    '''
    print(f"Your message: {message_to_disp}")


message: str = 'Hello'
display_message(message)
