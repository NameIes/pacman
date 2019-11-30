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

    pacman = Pacman(14 * z, 26 * z + z // 2)

    clock = pygame.time.Clock()
    # этот параметр нужен для отсчета времени старта
    counter_pacman = 0

    ghosts = [Blinky(12 * z + (z - 28) // 2, 17 * z + (z - 28) // 2),
              Pinky(12 * z + (z - 28) // 2, 18 * z + (z - 28) // 2),
              Inky(15 * z + (z - 28) // 2, 17 * z + (z - 28) // 2),
              Clyde(15 * z + (z - 28) // 2, 18 * z + (z - 28) // 2)]

    grain_array = []
    spawn_grain(pole_xy, grain_array)


    game_quit = False
    while not game_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
                screen.fill(black)
                pygame.display.flip()
                yellow = (255, 255, 0)  # желтый
                blue = (0, 0, 255)  # синий
                white = (255, 255, 255)  # белый
                fontObj = pygame.font.Font('freesansbold.ttf', 50)
                textSurfaceObj = fontObj.render('You Lose!', True, white)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (200, 200)

                screen.blit(textSurfaceObj, textRectObj)
                pygame.display.flip()
                pygame.time.delay(3000)



            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pacman.reaction(event)

                    # =========================================================== EXAMPLE
                if pygame.key.get_pressed()[pygame.K_f]:
                    for i in ghosts:
                        i.kill()

                if pygame.key.get_pressed()[pygame.K_g]:
                    for i in ghosts:
                        i.scared = True
                    # ===========================================================
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        pacman.action()
        pacman.teleport()
        screen.fill(black)

        show_field(screen, z)

        pacman.draw(screen)
        for grain in grain_array:
            grain.draw(screen)

        for i in ghosts:
            i.process_logic()
            i.process_draw(screen)

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
