import pygame
from objects.ghost import GhostBase


class Blinky(GhostBase):
    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None, speed=1):
        super().__init__(x, y, direction, anim_speed, pacman_rect, speed)
        self.images = [pygame.image.load('res/img/blinky_0.png'),
                       pygame.image.load('res/img/blinky_1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# При создании отдельного алгоритма движения, можно будет отнаследовать от Blinky
class Clyde(GhostBase):
    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None, speed=1):
        super().__init__(x, y, direction, anim_speed, pacman_rect, speed)
        self.images = [pygame.image.load('res/img/clyde_0.png'),
                       pygame.image.load('res/img/clyde_1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Inky(GhostBase):
    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None, speed=1):
        super().__init__(x, y, direction, anim_speed, pacman_rect, speed)
        self.images = [pygame.image.load('res/img/inky_0.png'),
                       pygame.image.load('res/img/inky_1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pinky(GhostBase):
    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None, speed=1):
        super().__init__(x, y, direction, anim_speed, pacman_rect, speed)
        self.images = [pygame.image.load('res/img/pinky_0.png'),
                       pygame.image.load('res/img/pinky_1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
