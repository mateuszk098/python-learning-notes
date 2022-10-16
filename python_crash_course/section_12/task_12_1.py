'''
Simple pygame blue window.
'''


import sys

import pygame


class BlueWindow():
    ''' Simple class representing a blue pygame window. '''

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen.fill((21, 24, 56))  # Blue screen.

    def run_game(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()  # Update of the screen.


if __name__ == '__main__':
    my_window = BlueWindow()
    my_window.run_game()
