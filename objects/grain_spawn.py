# -*- coding: utf-8 -*-
import pygame
import sys
from field.py import *


class Grain:
    grain_array = []

    def __init__(self, center_x, center_y, radius=2, color=(255, 255, 0)):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)

    def append(self):
        for count in range(0, 239):
            get_pos_in_field(x, y)
            self.center_x = xx
            self.center_y = yy
            self.grainArray.append(Grain((self.center_x, self.center_y), self.radius, self.color))


# class Energizer(Grain):

#    def __init__(self, center_x, center_y, radius = 2, color = (255, 255, 0)):
#        super().__init__(center_x, center_y)
#        self.radius = 7

#    def draw(self, screen):
#        pygame.draw.circle(screen, self.color,(self.center_x, self.center_y), self.radius)


# Функция постановки зёрен на поле
def spawn_grain(pole_xy, grain_array):
    count = 0
    for i in range(35):
        j = 0
        for j in range(27):
            if pole_xy[i][j] == 0 and pole_xy[i][j] == 3:
                pole_xy[i][j] = grain_array[count]


def check_grain(xx, yy, grain_array):
    for i in range(len(grain_array)):
        if (pole_xy[i][j] == grain_array[i]):
            return 'true'
        else:
            return 'false'


def main():
    size = (800, 600)
    black = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode(size)

    for i in range(len(pole_xy[yy][xx])):
        Grain.draw(xx, yy)
    # g1 = Grain(100, 100)
    # g2 = Energizer(50, 50)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)

        g1.draw(screen)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    main()
