import pygame
from objects.ghost import GhostBase


class Blinky(GhostBase):
    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None):
        super().__init__(x, y, direction, anim_speed, pacman_rect)
        self.images = [pygame.image.load('res/img/blinky_0.png'),
                       pygame.image.load('res/img/blinky_1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def process_logic(self):
        super().process_logic()
        # Место для алгоритма движения, и контролем над полями scared, is_death, speed


# При создании отдельного алгоритма движения, можно будет отнаследовать от Blinky
class Clyde(GhostBase):
    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None):
        super().__init__(x, y, direction, anim_speed, pacman_rect)
        self.images = [pygame.image.load('res/img/clyde_0.png'),
                       pygame.image.load('res/img/clyde_1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def process_logic(self):
        super().process_logic()
        # Место для алгоритма движения, и контролем над полями scared, is_death, speed


class Inky(GhostBase):
    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None):
        super().__init__(x, y, direction, anim_speed, pacman_rect)
        self.images = [pygame.image.load('res/img/inky_0.png'),
                       pygame.image.load('res/img/inky_1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def process_logic(self):
        super().process_logic()
        # Место для алгоритма движения, и контролем над полями scared, is_death, speed


class Pinky(GhostBase):
    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None):
        super().__init__(x, y, direction, anim_speed, pacman_rect)
        self.images = [pygame.image.load('res/img/pinky_0.png'),
                       pygame.image.load('res/img/pinky_1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def process_logic(self):
        super().process_logic()
        # Место для алгоритма движения, и контролем над полями scared, is_death, speed
