# -*- coding: utf-8 -*-
import pygame
import sys

blue = 0, 255, 0
black = 0, 0, 0


# a , b - координаты прямоугольника, w, h - ширина и высота, z - множитель, d - толщина линии , r - скругление углов, в пикселях
def rect_1(screen, color=(0, 0, 255), a=int(0), b=int(0), w=100, h=200, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, True, [[a + r, b], [a + w * z - r, b],
                                            [a + w * z, b + r], [a + w * z, b + h * z - r],
                                            [a + w * z - r, b + h * z], [a + r, b + h * z], [a, b + h * z - r],
                                            [a, b + r]], d)


# fig_1   #######
#
#
def fig_1(screen, color=(0, 0, 255), a=int(0), b=int(0), w=100, h=200, m=40, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, True,
                      [[a + r, b], [a + w * z - r, b], [a + w * z, b + r], [a + w * z, b + m * z - r],
                       [a + w * z - r, b + m * z], [a + w // 2 * z + m // 2 * z + r, b + m * z],
                       [a + w * z // 2 + m // 2 * z, b + m * z + r], [a + w * z // 2 + m // 2 * z, b + h * z - r],
                       [a + w * z // 2 + m // 2 * z - r, b + h * z], [a + w * z // 2 - m * z // 2 + r, b + h * z],
                       [a + w * z // 2 - m * z // 2, b + h * z - r], [a + w * z // 2 - m * z // 2, b + m * z + 6],
                       [a + w * z // 2 - m * z // 2 - r, b + m * z], [a + r, b + m * z], [a, b + m * z - r], [a, b + r]]
                      , d)


# fig_2      #
#
#######
def fig_2(screen, color=(0, 0, 255), a=int(0), b=int(0), w=100, h=200, m=40, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, True,
                      [[a + w // 2 * z - m // 2 + r, b], [a + w // 2 * z + m // 2 - r, b],
                       [a + w // 2 * z + m // 2, b + r], [a + w // 2 * z + m // 2, b + h * z - m * z - r],
                       [a + w // 2 * z + m // 2 + r, b + h * z - m * z], [a + w * z - r, b + h * z - m * z],
                       [a + w * z, b + h * z - m * z + r], [a + w * z, b + h * z - r], [a + w * z - r, b + h * z],
                       [a + r, b + h * z], [a, b + h * z - r], [a, b + h * z - m * z + r], [a + r, b + h * z - m * z],
                       [a + w // 2 * z - m // 2 - r, b + h * z - m * z],
                       [a + w // 2 * z - m // 2, b + h * z - m * z - r], [a + w // 2 * z - m // 2, b + r]]
                      , d)


# fig_2_2    #
#
#########

def fig_2_2(screen, color=(0, 0, 255), a=int(0), b=int(0), w=100, w1=50, h=200, m=40, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, True,
                      [[a + w1 * z - m // 2 + r, b], [a + w1 * z + m // 2 - r, b], [a + w1 * z + m // 2, b + r],
                       [a + w1 * z + m // 2, b + h * z - m * z - r], [a + w1 * z + m // 2 + r, b + h * z - m * z],
                       [a + w * z - r, b + h * z - m * z], [a + w * z, b + h * z - m * z + r],
                       [a + w * z, b + h * z - r], [a + w * z - r, b + h * z], [a + r, b + h * z], [a, b + h * z - r],
                       [a, b + h * z - m * z + r], [a + r, b + h * z - m * z],
                       [a + w1 * z - m // 2 - r, b + h * z - m * z], [a + w1 * z - m // 2, b + h * z - m * z - r],
                       [a + w1 * z - m // 2, b + r]]
                      , d)


# fig_3    #
#
####
#
#

def fig_3(screen, color=(0, 0, 255), a=int(0), b=int(0), w=100, h=200, m=40, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, True,
                      [[a + r, b], [a + m * z - r, b], [a + m * z, b + r], [a + m * z, b + h // 2 * z - m // 2 * z - r],
                       [a + m * z + r, b + h // 2 * z - m // 2 * z], [a + w * z - r, b + h // 2 * z - m // 2 * z],
                       [a + w * z, b + h // 2 * z - m // 2 * z + r], [a + w * z, b + h // 2 * z + m // 2 * z - r],
                       [a + w * z - r, b + h // 2 * z + m // 2 * z], [a + m * z + r, b + h // 2 * z + m // 2 * z],
                       [a + m * z, b + h // 2 * z + m // 2 * z + r], [a + m * z, b + h * z - r],
                       [a + m * z - r, b + h * z], [a + r, b + h * z], [a, b + h * z - r], [a, b + r]]
                      , d)


# fig_4    #
#
####
#
#
def fig_4(screen, color=(0, 0, 255), a=int(0), b=int(0), w=100, h=200, m=40, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, True,
                      [[a + r, b + h // 2 * z - m // 2 * z], [a + w * z - m * z - r, b + h // 2 * z - m // 2 * z],
                       [a + w * z - m * z, b + h // 2 * z - m // 2 * z - r], [a + w * z - m * z, b + r],
                       [a + w * z - m * z + r, b], [a + w * z - r, b], [a + w * z, b + r], [a + w * z, b + h * z - r],
                       [a + w * z - r, b + h * z], [a + w * z - m * z + r, b + h * z],
                       [a + w * z - m * z, b + h * z - r], [a + w * z - m * z, b + h // 2 * z + m // 2 * z + r],
                       [a + w * z - m * z - r, b + h // 2 * z + m // 2 * z], [a + r, b + h // 2 * z + m // 2 * z],
                       [a, b + h // 2 * z + m // 2 * z - r], [a, b + h // 2 * z - m // 2 * z + r]]
                      , d)


# fig_5 ####
#
#
def fig_5(screen, color=(0, 0, 255), a=int(0), b=int(0), w=100, h=200, m=40, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, True,
                      [[a + r, b], [a + w * z - r, b], [a + w * z, b + r], [a + w * z, b + h * z - r],
                       [a + w * z - r, b + h * z], [a + w * z - m * z + r, b + h * z],
                       [a + w * z - m * z, b + h * z - r], [a + w * z - m * z, b + m * z + r],
                       [a + w * z - m * z - r, b + m * z], [a + r, b + m * z], [a, b + m * z - r], [a, b + r]]
                      , d)


# fig_6    ####
#
#

def fig_6(screen, color=(0, 0, 255), a=int(0), b=int(0), w=100, h=200, m=40, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, True,
                      [[a + r, b], [a + w * z - r, b], [a + w * z, b + r], [a + w * z, b + m * z - r],
                       [a + w * z - r, b + m * z], [a + m * z + r, b + m * z], [a + m * z, b + m * z + r],
                       [a + m * z, b + h * z - r], [a + m * z - r, b + h * z], [a + r, b + h * z], [a, b + h * z - r],
                       [a, b + r]]
                      , d)


def angle_1(screen, color=(0, 0, 255), a=int(0), b=int(0), w=16, h=16, m=4, r=5, d=1, z=1, c=0):
    pygame.draw.lines(screen, color, False,
                      [[a, b + h * z], [a, b + r], [a + r, b], [a + w * z-c, b], ]
                      , d)
    pygame.draw.lines(screen, color, False,
                      [[a + m * z, b + h * z], [a + m * z, b + m * z + r], [a + m * z + r, b + m * z],
                       [a + w * z-c, b + m * z]]
                      , d)


def angle_2(screen, color=(0, 0, 255), a=int(0), b=int(0), w=16, h=16, m=4, r=5, d=1, z=1, c=0):
    pygame.draw.lines(screen, color, False,
                      [[a+c, b], [a + w * z - r, b], [a + w * z, b + r], [a + w * z, b + h * z]]
                      , d)
    pygame.draw.lines(screen, color, False,
                      [[a+c, b + m * z], [a + w * z - m * z - r, b + m * z], [a + w * z - m * z, b + m * z + r],
                       [a + w * z - m * z, b + h * z]]
                      , d)


def angle_3(screen, color=(0, 0, 255), a=int(0), b=int(0), w=16, h=16, m=4, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, False,
                      [[a, b], [a, b + h * z - r], [a + r, b + h * z], [a + w * z, b + h * z]]
                      , d)
    pygame.draw.lines(screen, color, False,
                      [[a + m * z, b], [a + m * z, b + h * z - m * z - r], [a + m * z + r, b + h * z - m * z],
                       [a + w * z, b + h * z - m * z]]
                      , d)


def angle_4(screen, color=(0, 0, 255), a=int(0), b=int(0), w=16, h=16, m=4, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, False,
                      [[a + w * z, b], [a + w * z, b + h * z - r], [a + w * z - r, b + h * z], [a, b + h * z]]
                      , d)
    pygame.draw.lines(screen, color, False,
                      [[a + w * z - m * z, b], [a + w * z - m * z, b + h * z - m * z - r],
                       [a + w * z - m * z - r, b + h * z - m * z], [a, b + h * z - m * z]]
                      , d)


def angle_5(screen, color=(0, 0, 255), a=int(0), b=int(0), w=16, h=16, m=4, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, False,
                      [[a + w * z, b], [a + w * z, b + h * z // 2 - m * z // 2 - r],
                       [a + w * z - r, b + h * z // 2 - m * z // 2], [a + r, b + h * z // 2 - m * z // 2],
                       [a, b + h * z // 2 - m * z // 2 + r], [a, b + h * z // 2 + m * z // 2 - r],
                       [a + r, b + h * z // 2 + m * z // 2], [a + w * z - r, b + h * z // 2 + m * z // 2],
                       [a + w * z, b + h * z // 2 + m * z // 2 + r], [a + w * z, b + h * z]]
                      , d)


def angle_6(screen, color=(0, 0, 255), a=int(0), b=int(0), w=16, h=16, m=4, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, False,
                      [[a, b], [a, b + h * z // 2 - m * z // 2 - r], [a + r, b + h * z // 2 - m * z // 2],
                       [a + w * z - r, b + h * z // 2 - m * z // 2], [a + w * z, b + h * z // 2 - m * z // 2 + r],
                       [a + w * z, b + h * z // 2 + m * z // 2 - r], [a + w * z - r, b + h * z // 2 + m * z // 2],
                       [a + r, b + h * z // 2 + m * z // 2], [a, b + h * z // 2 + m * z // 2 + r], [a, b + h * z]]
                      , d)


def angle_7(screen, color=(0, 0, 255), a=int(0), b=int(0), w=16, h=16, m=4, r=5, d=1, z=1):
    pygame.draw.lines(screen, color, False,
                      [[a, b], [a + w * z // 2 - m * z // 2 - r, b], [a + w * z // 2 - m * z // 2, b + r],
                       [a + w * z // 2 - m * z // 2, b + h * z - r], [a + w * z // 2 - m * z // 2 + r, b + h * z],
                       [a + w * z // 2 + m * z // 2 - r, b + h * z], [a + w * z // 2 + m * z // 2, b + h * z - r],
                       [a + w * z // 2 + m * z // 2, b + r], [a + w * z // 2 + m * z // 2 + r, b], [a + w * z, b]]
                      , d)


def draw_walls():
    pygame.init()
    size = width, height = 600, 800
    screen = pygame.display.set_mode(size)
    rect_1(screen, 30, 50)
    gameover = False

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        screen.fill(black)
        # rect_1(screen, 30, 50)
        # rect_1(screen, 130, 50, 300, 200, 5, 2)
        # fig_1(screen, 20, 30, 300, 200, 50, 5, 1)
        # fig_2(screen, 20, 130, 300, 200, 50, 5, 1)
        # fig_2_2(screen, 100, 130, 300,200, 200, 50, 5, 1)
        fig_6(screen, 20, 130, 300, 200, 50, 5, 1)
        # show_field(screen, pole_xy, (0, 0, 127))
        angle_1(screen, (0, 255, 0), 50, 30)
        angle_2(screen, (0, 255, 0), 300, 30)
        angle_3(screen, (0, 255, 0), 50, 300)
        angle_4(screen, (0, 255, 0), 300, 300)
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


# if __name__ == '__main__':
#     draw_walls()
