#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import math
import pygame.gfxdraw
from objects.field import pole_xy, z, is_cell_centre, get_pos_in_field
from objects.ghost import GhostBase

yellow = 255, 255, 0


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
        self.mouth_angle = 15
        self.animation = True  # Открывающийся рот True , закрывающийся False
        self.anim_cadr = 0
        self.anim_limit = 6
        self.speed = 1
        self.radius = z - 2
        self.standing = 0
        self.rotate_memory_dir = self.direction  # Запоминание направления

    def can_move_in(self, direction):
        xx, yy = get_pos_in_field(self.x, self.y)
        flag_center = is_cell_centre(self.x, self.y)
        res_flag = False
        # print("{} {} {}".format(xx,yy,("YES" if flag_center else "NO")))
        if direction == 'd':
            if pole_xy[yy][xx + 1] not in [1, 4] and pole_xy[yy][xx + 1] != 9:
                res_flag = True
            else:
                if flag_center:  # Если впереди стенами но мы не достигли центра клетки
                    res_flag = False
                else:
                    res_flag = True
        elif direction == 'a':
            if pole_xy[yy][xx - 1] not in [1, 4] and pole_xy[yy][xx - 1] != 8:
                res_flag = True
            else:
                if flag_center:  # Если впереди стенами но мы не достигли центра клетки
                    res_flag = False
                else:
                    res_flag = True
        elif direction == 'w':
            if pole_xy[yy - 1][xx] not in [1, 4]:
                res_flag = True
            else:
                if flag_center:  # Если впереди стенами но мы не достигли центра клетки
                    res_flag = False
                else:
                    res_flag = True
        elif direction == 's':
            if pole_xy[yy + 1][xx] not in [1, 4]:
                res_flag = True
            else:
                if flag_center:  # Если впереди стенами но мы не достигли центра клетки
                    res_flag = False
                else:
                    res_flag = True

        return res_flag

    def can_rotate(self, direction):
        xx, yy = get_pos_in_field(self.x, self.y)
        flag_center = is_cell_centre(self.x, self.y)
        res_flag = False

        if pole_xy[yy][xx] == 3:
            if flag_center:
                # self.direction = self.rotate_memory_dir
                res_flag = self.can_move_in(direction)
            else:
                # self.rotate_memory_dir = direction
                res_flag = False

        else:
            if self.direction == 'd' or self.direction == 'a':
                if direction == 'd' or direction == 'a':
                    res_flag = self.can_move_in(direction)
                else:
                    res_flag = False
            else:
                if direction == 'w' or direction == 's':
                    res_flag = self.can_move_in(direction)
                else:
                    res_flag = False

        return res_flag

    def reaction(self, event):
        pressed = pygame.key.get_pressed()
        # print("a - {} -rot {} -can_move_in ".format(
        #     ("YES" if self.can_move_in('a') else "NO"),
        #     ("YES" if self.can_rotate('a') else "NO")))
        # print("d - {} -rot {} -can_move_in ".format(
        #     ("YES" if self.can_move_in('d') else "NO"),
        #     ("YES" if self.can_rotate('d') else "NO")))
        # print("w - {} -rot {} -can_move_in ".format(
        #     ("YES" if self.can_move_in('w') else "NO"),
        #     ("YES" if self.can_rotate('w') else "NO")))
        # print("s - {} -rot {} -can_move_in ".format(
        #     ("YES" if self.can_move_in('s') else "NO"),
        #     ("YES" if self.can_rotate('s') else "NO")))

        if event.type == pygame.KEYDOWN:  # or event.type == pygame.KEYUP:
            k = 'f'
            if pressed[pygame.K_a]:
                k = 'a'
            if pressed[pygame.K_d]:
                k = 'd'
            if pressed[pygame.K_w]:
                k = 'w'
            if pressed[pygame.K_s]:
                k = 's'

            if k != 'f':
                xx, yy = get_pos_in_field(self.x, self.y)
                if pole_xy[yy][xx] == 3:
                    if not is_cell_centre(self.x, self.y):
                        self.rotate_memory_dir = k
                    else:
                        if self.can_rotate(k):
                            self.direction = k
                else:
                    if self.can_rotate(k):
                        self.direction = k

    def action(self, ):
        # TODO: повторяются вычисления положения в матрицы и её значение занести в класс
        xx, yy = get_pos_in_field(self.x, self.y)

        if self.start:
            if pole_xy[yy][xx] == 3 or pole_xy[yy][xx] == 8:
                if is_cell_centre(self.x, self.y):
                    if self.can_rotate(self.rotate_memory_dir):
                        self.direction = self.rotate_memory_dir
            else:
                self.rotate_memory_dir = self.direction

            if self.direction == 'w':
                if self.can_move_in('w'):
                    self.y -= self.speed
                    self.standing = 1
                else:
                    self.stop_anim()
            elif self.direction == 'a':
                if self.can_move_in('a'):
                    self.x -= self.speed
                    self.standing = 1
                else:
                    self.stop_anim()
            elif self.direction == 's':
                if self.can_move_in('s'):
                    self.y += self.speed
                    self.standing = 1
                else:
                    self.stop_anim()
            else:
                if self.can_move_in('d'):
                    self.x += self.speed
                    self.standing = 1
                else:
                    self.stop_anim()

            self.anim_cadr += self.standing
            if self.anim_cadr == self.anim_limit:
                self.anim_cadr = 0
                if self.mouth_angle == 15 and not self.animation:
                    self.animation = True
                elif self.mouth_angle == 75 and self.animation:
                    self.animation = False

                if self.animation:
                    self.mouth_angle += 15
                else:
                    self.mouth_angle -= 15

    def stop_anim(self):
        self.mouth_angle = 15
        self.anim_cadr = 0
        self.standing = 1

    def draw(self, screen):
        if not self.start:
            pygame.draw.circle(screen, yellow, (self.x, self.y), self.radius)
        else:
            p = [(self.x, self.y)]
            # Get points on arc
            start_angle, stop_angle = self.start_angles[self.direction]

            start_angle += self.mouth_angle
            stop_angle -= self.mouth_angle
            # print("{} {}".format(start_angle, stop_angle))

            p = [(self.x, self.y)]

            if start_angle < stop_angle:
                rang = list(range(start_angle, stop_angle))
            else:
                rang = list(range(start_angle, 360)) + list(
                    range(1, stop_angle))

            for n in rang:
                x1 = self.x + int(self.radius * math.cos(n * math.pi / 180))
                y1 = self.y + int(self.radius * math.sin(n * math.pi / 180))
                p.append((x1, y1))
            p.append((self.x, self.y))
            pygame.gfxdraw.filled_polygon(screen, p, yellow)

            # pygame.gfxdraw.pie(screen, self.y, self.y, self.radius, 15, 345,
            #                    yellow)

    def teleport(self):
        xx, yy = get_pos_in_field(self.x, self.y)
        R = True
        if pole_xy[yy][xx - 1] == 8 and R:
            self.x = 346
            self.y = 246
            R = False

        if pole_xy[yy][xx + 1] == 9 and R:
            self.x = 30
            self.y = 246
            R = False


def eat_or_be_eated(pacman, ghost):
    """Варианты исхода
    пакман наезжает или наезжает него наезжает приведение
    исхода пакман мертв - false

    пакман пересекается с напуганнымм приведением
    и мы его сеъедаем если наезжаем наезжаем него

    не забыть умножение награды забыть приведение забыть каждое
    съедение подряд.
    """
    pacman_live = True
    death_radius = 4
    px = pacman.x
    py = pacman.y

    gx = ghost.rect.centerx
    gy = ghost.rect.centery

    if (abs(px-gx) <= death_radius) and (abs(py-gy) <= death_radius):
        if ghost.scared:
            print("Pacman Eated Ghost")
            ghost.kill()
        elif ghost.is_dead:
            print("Toching dead things")
        else:
            print("You died")
            pacman_live = False

    return pacman_live
