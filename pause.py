import pygame
from objects.field import size
from ready import Text


def paused(screen):
    pause_flag = True
    text_pause = Text("PAUSE", 100)
    text_pause_size = text_pause.get_text_size()
    tx = (size[0] - text_pause_size[0]) // 2
    ty = (size[1] - text_pause_size[1]) // 2
    text_pause.update_position(tx, ty)

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
