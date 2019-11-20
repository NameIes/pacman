# -*- coding: utf-8 -*-

import sys
from objects.ghosts import *
from objects.field import FIELD_SIZE, pole_xy, show_field


def main():
    size = FIELD_SIZE
    black = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode(size)

    # TODO: подставлять координаты спавна приведений из нашего уровня

    lst = [
        Blinky(360, 220, direction='right'),
        Pinky(360, 220, direction='down'),
        Inky(360, 220, direction='left'),
        Clyde(360, 220, direction='up'),
    ]

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)

        show_field(screen, pole_xy, (0, 0, 127))
        for i in lst:
            i.process_logic()
            i.process_draw(screen)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    main()
