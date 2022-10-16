'''
Simple pygame window.
'''

import sys

import pygame


class Window():
    ''' Simple class representing a window. '''

    def __init__(self) -> None:
        ''' Game initialization. '''
        pygame.init()  # Initialize of the screen
        pygame.display.set_mode((1280, 720))

    def run_game(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                elif event.type == pygame.QUIT:
                    sys.exit()


if __name__ == '__main__':
    my_window: Window = Window()
    my_window.run_game()
