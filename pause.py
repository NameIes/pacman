import pygame
from objects.field import pole_xy, show_field, size
from ready import Text


def paused():
    pause_flag = True
    screen = pygame.display.set_mode(size)
    text_pause = Text("PAUSE", 100)
    text_pause_size = text_pause.get_text_size()
    text_pause.update_position(size[0] / 2 - text_pause_size[0] / 2, size[1] / 2 - text_pause_size[1] / 2)
    while pause_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == 'p':
                    pause_flag = False
        text_pause.draw(screen)
        pygame.display.update()