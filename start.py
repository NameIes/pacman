# -*- coding: utf-8 -*-

import sys
import pygame
from objects.ghosts import *
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

    lst = [
        #Blinky(x, y, direction='right'),
        #Pinky(x, y, direction='down'),
        #Inky(x, y, direction='left'),
        Clyde(12 * z + (z-28) // 2, 17 * z + (z-28) // 2, direction='up', speed=1)
    ]
    lst = [Blinky(12 * z + (z-28) // 2, 17 * z + (z-28) // 2, direction='up') for _ in range(20)]
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
