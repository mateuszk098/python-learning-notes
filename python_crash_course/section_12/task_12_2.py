'''
Simple pygame window with character on the screen.
'''

import sys

import pygame


class Alien():
    ''' Simple class representing alien ship on screen. '''

    def __init__(self) -> None:
        ''' Game initialization. '''
        pygame.init()  # Initialize of the screen
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()
        self.alien_image = pygame.image.load('alienship.png')
        self.alien_rect = self.alien_image.get_rect()
        self.alien_rect.midbottom = self.screen_rect.midbottom

    def run_game(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.blit(self.alien_image, self.alien_rect)
            pygame.display.flip()  # Update of the screen.


if __name__ == '__main__':
    my_alien: Alien = Alien()
    my_alien.run_game()
