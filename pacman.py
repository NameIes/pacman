#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys
import math
import pygame.gfxdraw
size = width, height = 800, 600
black = 0, 0, 0
yellow = 255, 255, 0
FPS = 60


class Pacman:
    start_angles = {
        'd': (0, 360),
        'a': (180, 180),
        'w': (270, 270),
        's': (90, 90)
    }

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = 'd'  # 'w', 'a', 's', 'd'
        self.start = False
        # TODO: Анимация
        # циклический кадр, 0 - шар, 1 - 5градусовы 2-10градусов
        # 3-15 градусов от направлющего вектора
        self.animation_cadr = 15
        self.animation_freq = 120
        self.speed = 2
        self.radius = 30

    def reaction(self, event):
        pressed = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_a]:
                self.direction = 'a'
            if pressed[pygame.K_d]:
                self.direction = 'd'
            if pressed[pygame.K_w]:
                self.direction = 'w'
            if pressed[pygame.K_s]:
                self.direction = 's'
        if event.type == pygame.KEYUP:
            pass

    def action(self, ):
        if self.start:
            if self.direction == 'w':
                self.y -= self.speed
            elif self.direction == 'a':
                self.x -= self.speed
            elif self.direction == 's':
                self.y += self.speed
            else:
                self.x += self.speed

    def draw(self, screen):
        # TODO: Рисовать круг пока игра не стартанула
        p = [(self.x, self.y)]
        # Get points on arc
        start_angle, stop_angle = self.start_angles[self.direction]

        start_angle += self.animation_cadr
        stop_angle -= self.animation_cadr
        # print("{} {}".format(start_angle, stop_angle))

        p = [(self.x, self.y)]

        if start_angle < stop_angle:
            rang = list(range(start_angle, stop_angle))
        else:
            rang = list(range(start_angle, 360)) + list(range(1, stop_angle))

        for n in rang:
            x1 = self.x + int(self.radius * math.cos(n * math.pi / 180))
            y1 = self.y + int(self.radius * math.sin(n * math.pi / 180))
            p.append((x1, y1))
        p.append((self.x, self.y))
        pygame.gfxdraw.filled_polygon(screen, p, yellow)
        # pygame.gfxdraw.pie(screen, self.y, self.y, self.radius, 15, 345,
        #                    yellow)


def main():
    main_screen = pygame.display.set_mode(size)
    game_quit = False

    pygame.init()

    P = Pacman(60, 60)

    clock = pygame.time.Clock()
    counter = 0

    while not game_quit:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                P.reaction(event)

        P.action()

        main_screen.fill(black)
        P.draw(main_screen)
        counter += 1
        if (counter > 100):
            P.start = True
        pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()
