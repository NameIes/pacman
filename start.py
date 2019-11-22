import sys
from grain import *
import pygame


def main():
    size = (800, 600)
    black = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode(size)

    g1 = Grain(50,50)
    g2 = Energizer(100, 100)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)

        g1.draw(screen)
        g2.draw(screen)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    main()