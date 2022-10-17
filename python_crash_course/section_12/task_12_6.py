'''
Moving spaceship, which can fire bullets.
'''

import sys

import pygame
from pygame.sprite import Sprite


class Ship():
    ''' Simple class representing a moving ship. '''

    def __init__(self) -> None:
        ''' Initialize game. '''
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()

        self.alien_image = pygame.image.load('alienship.png')
        self.alien_rect = self.alien_image.get_rect()
        self.alien_rect.midleft = self.screen_rect.midleft

        self.alien_moving_up: bool = False
        self.alien_moving_down: bool = False

        # Create bullets
        self.bullets = pygame.sprite.Group()

    def run_game(self) -> None:
        ''' Main loop of game. '''
        while True:
            self._check_events()
            self._update_ship()
            self._update_bullets()
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
        if event.key == pygame.K_UP:
            self.alien_moving_up = True
        elif event.key == pygame.K_DOWN:
            self.alien_moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event) -> None:
        ''' Reaction on key release. '''
        if event.key == pygame.K_UP:
            self.alien_moving_up = False
        elif event.key == pygame.K_DOWN:
            self.alien_moving_down = False

    def _update_ship(self) -> None:
        ''' Update alien ship on screen. '''
        if self.alien_moving_up and self.alien_rect.top > 0:
            self.alien_rect.y -= 2
        if self.alien_moving_down and self.alien_rect.bottom < self.screen_rect.bottom:
            self.alien_rect.y += 2

    def _fire_bullet(self) -> None:
        ''' Create new bullet and add it to group. '''
        new_bullet: Bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        ''' Update of bullets positions and remove bullets from out of screen. '''
        self.bullets.update()
        # Remove bullets out of the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen_rect.right:  # type: ignore
                self.bullets.remove(bullet)

    def _update_screen(self) -> None:
        ''' Updates the screen. '''
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.alien_image, self.alien_rect)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  # type: ignore
        pygame.display.flip()


class Bullet(Sprite):
    ''' Simple class representing a bullet. '''

    def __init__(self, my_ship) -> None:
        super().__init__()
        self.screen = my_ship.screen
        self.color = (255, 255, 255)

        # Create bullet rect and its position.
        self.rect: pygame.Rect = pygame.Rect(0, 0, 20, 5)
        self.rect.midright = my_ship.alien_rect.midright

    def update(self, *args, **kwargs) -> None:
        ''' Bullet movement of the screen. '''
        self.rect.x += 2

    def draw_bullet(self) -> None:
        ''' Displays bullet on the screen. '''
        pygame.draw.rect(self.screen, self.color, self.rect)


if __name__ == '__main__':
    ship: Ship = Ship()
    ship.run_game()
