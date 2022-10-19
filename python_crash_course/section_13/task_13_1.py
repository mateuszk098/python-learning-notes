''' Implementation of stars net. '''

import sys

import pygame
from pygame.sprite import Sprite


class Window():
    ''' Simple class representing stars on the screen. '''

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()
        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self) -> None:
        while True:
            self._update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _create_stars(self) -> None:
        ''' Create net of stars. '''
        star: Star = Star()
        star_width: int = star.rect.width  # type: ignore
        star_height: int = star.rect.height  # type: ignore

        stars_per_col: int = (self.screen_rect.width - 2*star_width) // (2*star_width)
        stars_per_row: int = (self.screen_rect.height - 2*star_height) // (2*star_height)

        for row in range(stars_per_row):
            for col in range(stars_per_col):
                star = Star()
                star.rect.x += star_width + 2*star_width*col  # type: ignore
                star.rect.y += star_height + 2*star_height*row  # type: ignore
                self.stars.add(star)

    def _update_screen(self) -> None:
        ''' Updates the screen. '''
        self.screen.fill((0, 0, 0))
        self.stars.draw(self.screen)
        pygame.display.flip()  # Update of the screen.


class Star(Sprite):
    ''' Simple class representing a star. '''

    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()


if __name__ == '__main__':
    window: Window = Window()
    window.run_game()
