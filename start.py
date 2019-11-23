# -*- coding: utf-8 -*-

import sys
from objects.ghosts import *
from objects.field import SIZE, pole_xy, show_field
from objects.pacman import *


def main():
    size = SIZE
    black = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode(size)
    pacman = Pacman(60, 60)

    clock = pygame.time.Clock()
    counter_pacman = 0

    # Пример
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
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pacman.reaction(event)
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
