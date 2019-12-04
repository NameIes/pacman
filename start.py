# -*- coding: utf-8 -*-
import sys
import pygame
from objects.ghosts import Blinky, Pinky, Inky, Clyde
from objects.field import size, pole_xy, show_field, z, \
    is_cell_centre, get_pos_in_field
from objects.grain_spawn import spawn_grain, check_and_remove_grain
from objects.pacman import Pacman, eat_or_be_eated
from highscore import highscore_table
from menu import main_menu
from pause import paused
from ready import Text
from objects.uipacman import ScoreLable, Health


def game(screen):
    black = (0, 0, 0)
    score = 0
    pacman = Pacman(14 * z, 26 * z + z // 2)

    # Initialize UI
    score = ScoreLable(size[0] // 2, 21)
    hp = Health(z / 2, size[1] - 2 * z)

    # Иницализация Pacman
    pacman_start_pos = (14 * z, 26 * z + z // 2)
    pacman = Pacman(*pacman_start_pos)

    # Инициализация Призраков
    gh_start_x1 = 12 * z + (z - 28) // 2
    gh_start_x2 = 15 * z + (z - 28) // 2
    gh_start_y1 = 18 * z + (z - 28) // 2
    gh_start_y2 = 17 * z + (z - 28) // 2

    ghosts = [
        Blinky(gh_start_x1, gh_start_y1, pacman),
        Pinky(gh_start_x2, gh_start_y1, pacman),
        Clyde(gh_start_x2, gh_start_y2, pacman)
    ]

    ghosts.append(Inky(gh_start_x1, gh_start_y2, pacman, ghosts[0]))

    # Инициализация зерен
    grain_array = []
    spawn_grain(pole_xy, grain_array)

    # Инициализация стенок поля, предв. отрисовка
    under_layer = pygame.Surface(size)
    show_field(under_layer, z)
    hp.draw(under_layer)

    game_over = False
    pause_flag = False

    # Инициализацмя надписи READY перед началом раунда
    display_text_until = pygame.time.get_ticks() + 3000
    text_object = Text("READY", 90)
    text_size = text_object.get_text_size()
    text_object.update_position(size[0] / 2 - text_size[0] / 2,
                                size[1] / 2 - text_size[1] / 2)

    while not game_over:
        # clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == 'p':
                    paused(screen)
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
        if is_cell_centre(pacman.x, pacman.y):
            pxx, pyy = get_pos_in_field(pacman.x, pacman.y)
            res_score = check_and_remove_grain(pxx, pyy, grain_array)
            if res_score != 0:
                score.update_value(score.value + res_score)
                if res_score == 50:  # Energizer
                    for i in ghosts:
                        i.scared = True

        pacman.teleport()

        # == Отрисовка ==
        screen.fill(black)
        screen.blit(under_layer, (0, 0))

        score.draw(screen)

        pacman.draw(screen)
        for grain in grain_array:
            grain.draw(screen)

        start_round = False
        i = 0
        while (i < len(ghosts)) and (not start_round):
            ghost = ghosts[i]
            ghost.process_logic()
            if not ghost.is_dead:
                pacman_live = eat_or_be_eated(pacman, ghost)
                if pacman_live:
                    if ghost.is_dead:
                        score.update_value(score.value + 200)
                        # TODO: множетель убийств
                else:
                    # Смерть пакмана начала нового раунда
                    hp.die()
                    display_text_until = pygame.time.get_ticks() + 3000
                    start_round = True
            ghost.process_draw(screen)
            if pacman.start:
                ghost.set_score(score.value)
            else:
                ghost.set_score(0)
            i += 1

        if start_round:
            pacman = Pacman(*pacman_start_pos)
            ghosts = [
                Blinky(gh_start_x1, gh_start_y1, pacman),
                Pinky(gh_start_x2, gh_start_y1, pacman),
                Clyde(gh_start_x2, gh_start_y2, pacman)
            ]
            ghosts.append(Inky(gh_start_x1, gh_start_y2, pacman, ghosts[0]))
            start_round = False
            under_layer.fill(black)
            show_field(under_layer, z)
            hp.draw(under_layer)

        if pygame.time.get_ticks() < display_text_until:
            text_object.draw(screen)
        else:
            pacman.start = True

        pygame.display.flip()
        pygame.time.wait(20)

        if hp.value == 0:
            game_over = True
            pass  # TODO: Поражение

        if len(grain_array) == 0:
            game_over = True
            pass  # TODO: Победа

    sys.exit(0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    main_menu(screen, game, highscore_table)


if __name__ == '__main__':
    main()
