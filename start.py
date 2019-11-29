# -*- coding: utf-8 -*-

import sys
import pygame
from objects.ghosts import *
from objects.field import size, pole_xy, show_field, z
from objects.pacman import Pacman
from menu import main_menu


def game(screen):
    black = (0, 0, 0)

    pacman = Pacman(14 * z, 26 * z + z // 2)

    # clock = pygame.time.Clock()
    # этот параметр нужен для отсчета времени старта
    counter_pacman = 0

    ghosts = [Blinky(12 * z + (z - 28) // 2, 17 * z + (z - 28) // 2),
              Pinky(12 * z + (z - 28) // 2, 18 * z + (z - 28) // 2),
              Inky(15 * z + (z - 28) // 2, 17 * z + (z - 28) // 2),
              Clyde(15 * z + (z - 28) // 2, 18 * z + (z - 28) // 2)]

    game_over = False
    while not game_over:
        # clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pacman.reaction(event)

                # =========================================================== EXAMPLE
                if pygame.key.get_pressed()[pygame.K_f]:
                    for i in ghosts:
                        i.kill()
                # ===========================================================
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        pacman.action()

        screen.fill(black)

        show_field(screen, z)

        for i in ghosts:
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
