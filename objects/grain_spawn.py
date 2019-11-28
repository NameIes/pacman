# -*- coding: utf-8 -*-
import pygame
import sys
from field import pole_xy, get_pos_in_field, z, size

grain_array = []


class Grain:

    def __init__(self, center_x, center_y, radius=2, color=(255, 255, 0)):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)

    def append(self):
        for count in range(0, 239):
            x = j*z + z//2
            y = i*z + z//2
            grain_array.append(Grain(x,y))


# class Energizer(Grain):

#    def __init__(self, center_x, center_y, radius = 2, color = (255, 255, 0)):
#        super().__init__(center_x, center_y)
#        self.radius = 7

#    def draw(self, screen):
#        pygame.draw.circle(screen, self.color,(self.center_x, self.center_y), self.radius)


# Функция постановки зёрен на поле
def spawn_grain(xx, yy, pole_xy, grain_array):
    for i in range(35):
        for j in range(27):
            if pole_xy[yy][xx] == 0 and pole_xy[yy][xx] == 3:
                pole_xy[yy][xx] = grain_array


def check_grain(x, y, xx, yy, grain_array):
    for i in range(len(grain_array)):
        x = xx * z + z//2
        y = yy * z + z//2
    if grain.center_y == y and grain.center_x == x:
        return True
    else:
        return False


def main():
    size = (800, 600)
    black = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode(size)

    for grain in grain_array:
        grain.draw(screen)

    # g2 = Energizer(50, 50)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)

        #g1.draw(screen)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    main()
