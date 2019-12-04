# -*- coding: utf-8 -*-
import pygame
import sys
from objects.field import pole_xy, z, size


class Grain:
    def __init__(self, center_x, center_y, radius=2, color=(255, 255, 0)):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y),
                           self.radius)


class Energizer(Grain):
    def __init__(self, center_x, center_y, radius=2, colors=[(255, 255, 0), (255, 255, 155)]):
        super().__init__(center_x, center_y)
        self.radius = 7
        self.anim = False
        self.anim_timer = 0
        self.colors = colors

    def draw(self, screen):
        self.anim_timer += 1

        if self.anim_timer == 10:
            self.radius += 1 if self.anim else -1
            self.color = self.colors[0 if self.anim else 1]
            self.anim_timer = 0

        if self.radius == 7:
            self.anim = False
        if self.radius == 4:
            self.anim = True

        pygame.draw.circle(screen, self.color, (self.center_x, self.center_y),
                           self.radius)


# Функция постановки зёрен на поле
def spawn_grain(pole_xy, grain_array):
    for i in range(len(pole_xy)):
        for j in range(len(pole_xy[0])):
            if pole_xy[i][j] == 0 or pole_xy[i][j] == 3 or pole_xy[i][j] == 8:
                x = j * z + z // 2
                y = i * z + z // 2
                # Действует только для текущего поля
                if (i == 6 or i == 26) and (j == 1 or j == 26):
                    grain_array.append(Energizer(x, y))
                else:
                    if ((i == 17) and (j < 6)):
                        pass
                    elif ((i == 17) and (j > 21)):
                        pass
                    elif (i > 11 and i < 23) and (j > 7 and j < 21):
                        pass
                    elif j == 14 and i == 26:
                        pass
                    else:
                        grain_array.append(Grain(x, y))


def check_and_remove_grain(xx, yy, grain_array):
    x = xx * z + z // 2
    y = yy * z + z // 2
    flag_res = 0
    for grain in grain_array:
        if grain.center_y == y and grain.center_x == x:
            if grain.radius in [4, 5, 6, 7]:  # Это на случай вишни
                # print("Eated")
                flag_res = 50
            else:
                flag_res = 10
            grain_array.remove(grain)

    return flag_res

def main():
    black = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode(size)

    grain_array = []
    spawn_grain(pole_xy, grain_array)
    print(len(grain_array))

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)
        for grain in grain_array:
            grain.draw(screen)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    main()
