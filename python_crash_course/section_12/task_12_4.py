''' 
Simple pygame window with moving ship.
'''

import sys

import pygame


class Ship():
    ''' Simple class representing moving ship. '''

    def __init__(self) -> None:
        ''' Initialization '''
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()

        self.alien_image = pygame.image.load('alienship.png')
        self.alien_rect = self.alien_image.get_rect()
        self.alien_rect.center = self.screen_rect.center

        self.alien_moving_right: bool = False
        self.alien_moving_left: bool = False
        self.alien_moving_up: bool = False
        self.alien_moving_down: bool = False

    def run_game(self) -> None:
        ''' Main loop of the game. '''
        while True:
            self._check_events()
            self._update_alien()
            self._update_screen()

    def _check_events(self) -> None:
        ''' Check reaction to button press and mouse interaction. '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        ''' Reaction on key press. '''
        if event.key == pygame.K_RIGHT:
            self.alien_moving_right = True
        elif event.key == pygame.K_LEFT:
            self.alien_moving_left = True
        elif event.key == pygame.K_UP:
            self.alien_moving_up = True
        elif event.key == pygame.K_DOWN:
            self.alien_moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event) -> None:
        ''' Reaction on key release. '''
        if event.key == pygame.K_RIGHT:
            self.alien_moving_right = False
        elif event.key == pygame.K_LEFT:
            self.alien_moving_left = False
        elif event.key == pygame.K_UP:
            self.alien_moving_up = False
        elif event.key == pygame.K_DOWN:
            self.alien_moving_down = False

    def _update_alien(self) -> None:
        ''' Update alien ship on screen. '''
        if self.alien_moving_right and self.alien_rect.right < self.screen_rect.right:
            self.alien_rect.x += 2
        if self.alien_moving_left and self.alien_rect.left > 0:
            self.alien_rect.x -= 2
        if self.alien_moving_up and self.alien_rect.top > 0:
            self.alien_rect.y -= 2
        if self.alien_moving_down and self.alien_rect.bottom < self.screen_rect.bottom:
            self.alien_rect.y += 2

    def _update_screen(self) -> None:
        ''' Updates the screen. '''
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.alien_image, self.alien_rect)
        pygame.display.flip()  # Update of the screen.


if __name__ == '__main__':
    ship: Ship = Ship()
    ship.run_game()
