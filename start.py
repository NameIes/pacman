import sys
from objects.ghosts import *


def main():
    size = (800, 600)
    black = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode(size)

    # Пример
    lst = [Blinky(10, 10, direction='right'), Pinky(750, 10, direction='down'), Inky(750, 550, direction='left'),
           Clyde(10, 550, direction='up'), Blinky(300, 200, direction='right'), Blinky(500, 400, direction='left')]
    lst[-2].scared = True
    lst[-1].is_death = True
    #

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)

        # Пример
        for i in lst:
            i.process_logic()
            i.process_draw(screen)
        #

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    main()