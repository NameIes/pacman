# -*- coding: utf-8 -*-

import sys
import pygame
from objects.ghosts import *
from objects.field import size, pole_xy, show_field, z
from objects.grain_spawn import spawn_grain
from objects.pacman import Pacman
from menu import main_menu


def game(screen):
    black = (0, 0, 0)

    pacman = Pacman(14*z, 26*z + z//2)

    # clock = pygame.time.Clock()
    # этот параметр нужен для отсчета времени старта
    counter_pacman = 0

    # TODO: подставлять координаты спавна приведений из нашего уровня

    lst = [Blinky(12 * z + (z-28) // 2, 17 * z + (z-28) // 2, direction='up') for _ in range(20)]

    grain_array = []
    spawn_grain(pole_xy, grain_array)

    game_over = False
    while not game_over:
        # clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pacman.reaction(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        pacman.action()
        pacman.teleport()
        screen.fill(black)

        show_field(screen, z)
        for grain in grain_array:
            grain.draw(screen)
        for i in lst:
            i.process_logic()
            i.process_draw(screen)

        pacman.draw(screen)
        counter_pacman += 1

        if counter_pacman > 100:
            pacman.start = True

        pygame.display.flip()
        pygame.time.wait(20)

    sys.exit(0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    main_menu(screen, game)
    # game(screen)


if __name__ == '__main__':
    main()
