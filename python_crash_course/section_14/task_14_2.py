''' Spaceship shoots to the target. '''


import sys
from time import sleep

import pygame
from pygame.sprite import Sprite


class Shooter():
    ''' Class representing whole game. '''

    def __init__(self) -> None:
        ''' Initialize game. '''
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()

        self.user_ship: Ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target: Target = Target(self)
        self.play_button: Button = Button(self, 'Play')

        self.game_active: bool = False

    def run_game(self) -> None:
        ''' Main loop of the game. '''
        while True:
            self._check_events()

            if self.game_active is True:
                self.user_ship.update_ship()
                self._update_bullets()
                self._update_target()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event) -> None:
        ''' Reaction on key press. '''
        if event.key == pygame.K_UP:
            self.user_ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.user_ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.bullets.add(Bullet(self))

    def _check_keyup_events(self, event) -> None:
        ''' Reaction on key release. '''
        if event.key == pygame.K_UP:
            self.user_ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.user_ship.moving_down = False

    def _check_play_button(self, mouse_pos: tuple[int, int]) -> None:
        ''' Checks if the play button is clicked by mouse. '''
        button_clicked: bool = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked is True and self.game_active is False:
            self.game_active = True
            self.bullets.empty()
            pygame.mouse.set_visible(False)

    def _update_bullets(self) -> None:
        ''' Update of bullets positions and remove bullets from out of screen. '''
        self.bullets.update()
        # Remove bullets out of the screen.
        for bullet in self.bullets.copy():
            if pygame.sprite.collide_rect(self.target, bullet) is True:  # type: ignore
                self.bullets.remove(bullet)
            elif bullet.rect.right >= self.screen_rect.right:  # type: ignore
                self.bullets.remove(bullet)
                self.target.miss_hits -= 1
                if self.target.miss_hits <= 0:
                    self._check_game_end()

    def _check_game_end(self) -> None:
        ''' Reset game is player miss the target 3 times. '''
        sleep(1.0)
        self.bullets.empty()
        self.target.miss_hits = 3
        self.target.rect.midright = self.screen_rect.midright
        self.target.rect.x = self.screen_rect.width - 100
        self.target.y = float(self.target.rect.y)
        self.user_ship.rect.midleft = self.screen_rect.midleft
        self.game_active = False
        pygame.mouse.set_visible(True)

    def _update_target(self) -> None:
        self.target.update_target()
        if self.target.check_edges() is True:
            self.target.direction *= -1

    def _update_screen(self) -> None:
        ''' Updates the screen. '''
        self.screen.fill((0, 0, 0))
        self.user_ship.blit_ship()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  # type: ignore

        self.target.draw_target()

        if self.game_active is False:
            self.play_button.draw_button()

        pygame.display.flip()


class Ship():
    ''' Class representing the user spaceship. '''

    def __init__(self, sgame) -> None:
        ''' Initialization of spaceship and its initial position. '''
        self.screen = sgame.screen
        self.screen_rect = sgame.screen.get_rect()
        # Load the spaceship image and load its rect.
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()
        # Every new spaceship occurs at te bottom of the screen.
        self.rect.midleft = self.screen_rect.midleft
        # Position and moving.
        self.y: float = float(self.rect.y)  # Position is represented as a float
        self.moving_up: bool = False
        self.moving_down: bool = False

    def update_ship(self) -> None:
        ''' Update of the spaceship position considering flag indicating its moving. '''
        if self.moving_up is True and self.rect.top >= 0:
            self.y -= 1
        if self.moving_down is True and self.rect.bottom <= self.screen_rect.bottom:
            self.y += 1
        self.rect.y = int(self.y)

    def blit_ship(self) -> None:
        ''' Displays the spaceship in current position on the screen. '''
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    ''' Represents bullet fired by a spaceship. '''

    def __init__(self, sgame) -> None:
        ''' Create bullet in current spaceship position. '''
        super().__init__()
        self.screen = sgame.screen
        self.color: tuple[int, ...] = (255, 255, 255)
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = sgame.user_ship.rect.midright
        self.x: float = float(self.rect.x)

    def update(self, *args, **kwargs) -> None:
        ''' Bullet movement of the screen. '''
        self.x += 2
        self.rect.x = int(self.x)  # type: ignore

    def draw_bullet(self) -> None:
        ''' Displays bullet on the screen. '''
        pygame.draw.rect(self.screen, self.color, self.rect)  # type: ignore


class Target():
    ''' Class representing a target we have to shoot. '''

    def __init__(self, sgame) -> None:
        super().__init__()
        self.screen = sgame.screen
        self.screen_rect = sgame.screen.get_rect()
        self.color: tuple[int, ...] = (255, 255, 255)
        self.rect = pygame.Rect(0, 0, 15, 100)
        self.rect.midright = self.screen_rect.midright
        self.rect.x = self.screen_rect.width - 100
        self.y: float = float(self.rect.y)
        self.direction: int = 1
        self.miss_hits: int = 3

    def check_edges(self) -> bool:
        ''' Returns true if target is near the edge of the screen. '''
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
            return True
        return False

    def update_target(self) -> None:
        ''' Updates the target position. '''
        self.y += 0.1*self.direction
        self.rect.y = int(self.y)

    def draw_target(self) -> None:
        ''' Displays the target in current position on the screen. '''
        pygame.draw.rect(self.screen, self.color, self.rect)  # type: ignore


class Button():
    def __init__(self, sgame, msg) -> None:
        self.screen = sgame.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)  # type: ignore

        self.rect = pygame.Rect(0, 0, self.width, self.height)  # type: ignore
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def draw_button(self) -> None:
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _prep_msg(self, msg) -> None:
        ''' Puts message on the rect and center the message. '''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


if __name__ == '__main__':
    my_shooter: Shooter = Shooter()
    my_shooter.run_game()
