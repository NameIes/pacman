import sys
import pygame
from ready import Text
from objects.field import size

# screen = pygame.display.set_mode(size)


def button(x, y,
           width, height,
           inactive_colour,
           active_colour,
           screen, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_colour, (x, y, width, height))
        if click[0] and action is not None:
            action(screen)
    else:
        pygame.draw.rect(screen, inactive_colour, (x, y, width, height))


def exit(screen):
    pygame.display.quit()
    pygame.quit()
    quit()


def main_menu(screen, game_action=None, high_score_action=None):
    # size = (800, 600)
    black = 0, 0, 0
    blue = 0, 0, 255
    bright_blue = 0, 0, 150

    # pygame.init()

    game_over = False

    text_object1 = Text("PLAY", 30)
    text_size = text_object1.get_text_size()
    # TODO: добавил кортеж параметров кнопки ,переписать все через него
    btn1 = (size[0] / 2 - text_size[0] / 2, size[1] - text_size[1] / 2 - 425,
            text_size[0], text_size[1])
    text_object1.update_position(size[0] / 2 - text_size[0] / 2,
                                 size[1] - 425 - text_size[1] / 2)

    text_object2 = Text("HIGHSCORES", 30)
    text_size = text_object2.get_text_size()
    btn2 = (size[0] / 2 - text_size[0] / 2, size[1] - text_size[1] / 2 - 350,
            text_size[0], text_size[1])
    text_object2.update_position(size[0] / 2 - text_size[0] / 2,
                                 size[1] - 350 - text_size[1] / 2)

    text_object3 = Text("EXIT", 30)
    text_size = text_object3.get_text_size()
    btn3 = (size[0] / 2 - text_size[0] / 2, size[1] - text_size[1] / 2 - 275,
            text_size[0], text_size[1])
    text_object3.update_position(size[0] / 2 - text_size[0] / 2,
                                 size[1] - 275 - text_size[1] / 2)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)
        # DONE: Исправить абсолютные пути
        # button(325, 150, 145, 50, bright_blue, blue, screen, game_action)
        button(*btn1, bright_blue, blue, screen, game_action)
        # TODO добавить в строку ниже вызов функции "Таблица Highscores"
        button(*btn2, bright_blue, blue, screen, high_score_action)
        button(*btn3, bright_blue, blue, screen, exit)
        text_object1.draw(screen)
        text_object2.draw(screen)
        text_object3.draw(screen)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


# if __name__ == '__main__':
#     menu()
