# -*- coding: utf-8 -*-

import sys
import pygame
from objects.ghosts import Blinky, Pinky, Inky, Clyde
from objects.field import size, pole_xy, show_field, z
from objects.pacman import Pacman


def main():
    black = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode(size)
    pacman = Pacman(14*z, 26*z + z//2)

    # clock = pygame.time.Clock()
    # этот параметр нужен для отсчета времени старта
    counter_pacman = 0

    # TODO: подставлять координаты спавна приведений из нашего уровня
    lst = [
        Blinky(10, 10, direction='right'),
        Pinky(750, 10, direction='down'),
        Inky(750, 550, direction='left'),
        Clyde(10, 550, direction='up'),
        Blinky(300, 200, direction='right'),
        Blinky(500, 400, direction='left')
    ]
    lst[-2].scared = True
    lst[-1].is_death = True
    #

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

        screen.fill(black)

        show_field(screen, pole_xy, (0, 0, 127))
        # Пример
        for i in lst:
            i.process_logic()
            i.process_draw(screen)

        pacman.draw(screen)
        counter_pacman += 1

        if counter_pacman > 100:
            pacman.start = True

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    main()
