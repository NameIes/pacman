import pygame
from objects.ghost import GhostBase


class Blinky(GhostBase):
    def __init__(self, x, y, pacman_obj=None, move_speed=1, anim_speed=10, direction='up'):
        super().__init__(x, y, 'blinky', pacman_obj, move_speed, anim_speed, direction)


class Clyde(GhostBase):
    def __init__(self, x, y, pacman_obj=None, move_speed=1, anim_speed=10, direction='up'):
        super().__init__(x, y, 'clyde', pacman_obj, move_speed, anim_speed, direction)


class Inky(GhostBase):
    def __init__(self, x, y, pacman_obj=None, move_speed=1, anim_speed=10, direction='up'):
        super().__init__(x, y, 'inky', pacman_obj, move_speed, anim_speed, direction)


class Pinky(GhostBase):
    def __init__(self, x, y, pacman_obj=None, move_speed=1, anim_speed=10, direction='up'):
        super().__init__(x, y, 'pinky', pacman_obj, move_speed, anim_speed, direction)
