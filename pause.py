import pygame
from objects.field import FIELD_SIZE, pole_xy, show_field, size


def paused():
    pause_flag = True
    while pause_flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == 'p':
                    pause_flag = False
