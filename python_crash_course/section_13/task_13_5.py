'''
Moving spaceship, which can fire bullets and shots alien.
'''

import sys
import random

import pygame
from pygame.sprite import Sprite


class AlienGame():
    ''' Simple class representing game with shooting to alien. '''

    def __init__(self) -> None:
        ''' Initialize game. '''
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()

        self.ship_image = pygame.image.load('spaceship.png')
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.midleft = self.screen_rect.midleft

        self.ship_moving_up: bool = False
        self.ship_moving_down: bool = False

        self.bullets = pygame.sprite.Group()

        alien: Alien = Alien(self)
        self.aliens = pygame.sprite.Group()
        self.aliens.add(alien)

    def run_game(self) -> None:
        ''' Main loop of game. '''
        while True:
            self._check_events()
            self._update_ship()
            self._update_bullets()
            self._update_aliens()
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
            self.ship_moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship_moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event) -> None:
        ''' Reaction on key release. '''
        if event.key == pygame.K_UP:
            self.ship_moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship_moving_down = False

    def _update_ship(self) -> None:
        ''' Update ship on screen. '''
        if self.ship_moving_up and self.ship_rect.top > 0:
            self.ship_rect.y -= 2
        if self.ship_moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_rect.y += 2

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

        # Remove bullet and alien when they collide.
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _check_alien_edges(self) -> None:
        ''' Reaction if any alien comes to the screen edge. '''
        for alien in self.aliens.sprites():
            if alien.check_edges() is True:  # type: ignore
                alien.rect.x -= 10  # type: ignore
                alien.direction *= -1  # type: ignore
                break

    def _update_aliens(self) -> None:
        ''' Update all aliens position on the screen. '''
        self._check_alien_edges()
        self.aliens.update()

    def _update_screen(self) -> None:
        ''' Updates the screen. '''
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.ship_image, self.ship_rect)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  # type: ignore

        self.aliens.draw(self.screen)
        pygame.display.flip()


class Bullet(Sprite):
    ''' Simple class representing a bullet. '''

    def __init__(self, my_ship) -> None:
        super().__init__()
        self.screen = my_ship.screen
        self.color = (255, 255, 255)

        # Create bullet rect and its position.
        self.rect: pygame.Rect = pygame.Rect(0, 0, 20, 5)
        self.rect.midright = my_ship.ship_rect.midright

    def update(self, *args, **kwargs) -> None:
        ''' Bullet movement of the screen. '''
        self.rect.x += 2

    def draw_bullet(self) -> None:
        ''' Displays bullet on the screen. '''
        pygame.draw.rect(self.screen, self.color, self.rect)


class Alien(Sprite):
    ''' Simple class representing a alien. '''

    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('alienship.png')
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(self.screen_rect.width//2, self.screen_rect.width)
        self.rect.y = random.randint(0, self.screen_rect.height)

        self.direction: int = 1

    def check_edges(self) -> bool:
        ''' Returns true if alien ship is near the edge of the screen. '''
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:  # type: ignore
            return True
        return False

    def update(self, *args, **kwargs) -> None:
        ''' Updates the alien position. '''
        self.rect.y += 1*self.direction  # type: ignore


if __name__ == '__main__':
    my_game: AlienGame = AlienGame()
    my_game.run_game()
