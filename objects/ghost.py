import pygame
import random
from objects.field import pole_xy
from start import start_position


class GhostBase:
    scared = 'res/img/scared.png'
    direction_vector = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}

    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None, speed=1):
        self.pacman_rect = pacman_rect  # Будет нужно для ИИ движения

        self.images = None
        self.image = None
        self.rect = None

        self.anim_speed = anim_speed
        self.timer = 0
        self.anim_stage = True

        self.direction = direction
        self.direction_speed = GhostBase.direction_vector.copy()
        self.set_speed(speed)
        self.scared = False
        self.is_dead = False

    def set_speed(self, speed):
        for item in self.direction_speed:
            self.direction_speed[item][0] *= speed
            self.direction_speed[item][1] *= speed

    def scared_move(self):
        # TODO: Реализовать движение при испуге
        pass

    def death_move(self): #требует доработки
        #движение на спавн после смерти

        #выбор направления движения

        x_spawn, y_spawn = start_position()
        x_spawn /= 14
        y_spawn /= 14
        #выбор приоритетного движения для призрака (в какую сторону надо двигаться, чтобы путь до спавна был самый короткий)

        if x > x_spawn:
            priority_rl = 'left'
        elif x < x_spawn:
            priority_rl = 'right'
        else:
            priority_rl = 'no'

        if y > y_spawn:
            priority_ud = 'up'
        elif y < y_spawn:
            priority_ud = 'down'
        else:
            priority_ud = 'no'


        #выбор направения (желательно приоритетного)
        if int ( pole_xy[y - 1][x] ) == 1 or int ( pole_xy[y - 2][x] ) == 1 or self.direction == 'down' :
            turn_up = False
        if int ( pole_xy[y + 1][x] ) == 1 or int ( pole_xy[y + 2][x] ) == 1 or self.direction == 'up' :
            turn_down = False
        if int ( pole_xy[y][x + 1] ) == 1 or int ( pole_xy[y][x + 2] ) == 1 or self.direction == 'left' :
            turn_right = False
        if int ( pole_xy[y][x - 1] ) == 1 or int ( pole_xy[y][x - 2] ) == 1 or self.direction == 'right' :
            turn_left = False
        #проверка, может ли призрак сразу дивагться в сторону спавна
        if turn_up and priority_ud == 'up':
            self.direction = 'up'
            return
        if turn_down and priority_ud == 'down':
            self.direction = 'down'
            return
        if turn_left and priority_rl == 'left':
            self.direction = 'left'
            return
        if turn_right and priority_rl == 'right':
            self.direction = 'right'
            return
        #если не может, то выбирается случайное направление
        dir = random.randint(1, 4)
        if dir == 1 and turn_right :
            self.direction = 'right'
            return
        elif dir == 2 and turn_left :
            self.direction = 'left'
            return
        elif dir == 3 and turn_up :
            self.direction = 'up'
            return
        elif dir == 4 and turn_down :
            self.direction = 'down'
            return

    def image_controller(self):
        if not self.scared or self.is_dead:  # Анимация
            self.timer += 1
            if self.timer == self.anim_speed:
                self.image = self.images[1 if self.anim_stage else 0]

                self.anim_stage = not self.anim_stage
                self.timer = 0
        elif self.scared:  # Напуган, когда съедено большое зерно
            self.image = pygame.image.load(GhostBase.scared)

    def process_logic(self):
        # алгоритм дфижения по коридорам
        x = int ( self.rect.x / 14 ) # нахожу x и y(в матрцице призраки находятся внутри портала)
        y = int ( self.rect.y / 14 )
        print(x, y, pole_xy[y][x])
        if int(pole_xy[y][x]) == 1:
            if self.direction == 'up':
                y += 1
                self.rect.y = y * 14
            if self.direction == 'down':
                y -= 1
                self.rect.y = y * 14
            if self.direction == 'left':
                x += 1
                self.rect.x = x * 14
            if self.direction == 'right':
                x -= 1
                self.rect.x = x * 14

        turn_right = True # 1 - номер направления при случайном выборе
        turn_left = True # 2 - номер направления при случайном выборе
        turn_up = True # 3 - номер направления при случайном выборе
        turn_down = True # 4 - номер направления при случайном выборе

        if int(pole_xy[y][x]) == 3 or int(pole_xy[y][x]) == 5:
            print(x, y, pole_xy[y][x], self.direction) # проверял x и y
            if self.is_dead :
                self.death_move ( x, y, turn_up, turn_right, turn_down, turn_left )
            else :
                # выбор направления движения

                # проверка всех возможных путей

                if int ( pole_xy[y - 1][x] ) == 1 or int ( pole_xy[y - 2][x] ) == 1 or self.direction == 'down' :
                    turn_up = False
                if int ( pole_xy[y + 1][x] ) == 1 or int ( pole_xy[y + 2][x] ) == 1 or self.direction == 'up' :
                    turn_down = False
                if int ( pole_xy[y][x + 1] ) == 1 or int ( pole_xy[y][x + 2] ) == 1 or self.direction == 'left' :
                    turn_right = False
                if int ( pole_xy[y][x - 1] ) == 1 or int ( pole_xy[y][x - 2] ) == 1 or self.direction == 'right' :
                    turn_left = False

                # случайный выбор направления
                dir = random.randint ( 1, 4 )
                if dir == 1 and turn_right :
                    self.direction = 'right'
                elif dir == 2 and turn_left :
                    self.direction = 'left'
                elif dir == 3 and turn_up :
                    self.direction = 'up'
                elif dir == 4 and turn_down :
                    self.direction = 'down'

        self.rect.x += self.direction_speed[self.direction][0]
        self.rect.y += self.direction_speed[self.direction][1]

        self.image_controller()

    def _set_pupil_pos(self, screen, left, right):
        pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + left[0], self.rect[1] + left[1], 4, 5))
        pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + right[0], self.rect[1] + right[1], 4, 5))

    def process_draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
        # Когда съеден пакманом, на базу бегут только глаза
        if not self.is_dead:
            screen.blit(self.image, self.rect)

        if self.scared:
            return

        # Глаза
        pygame.draw.ellipse(screen, (255, 255, 255), (self.rect[0] + 4, self.rect[1] + 6, 8, 10))
        pygame.draw.ellipse(screen, (255, 255, 255), (self.rect[0] + 16, self.rect[1] + 6, 8, 10))

        # Зрачки поворачиваются в сторону движения
        if self.direction == 'up':
            self._set_pupil_pos(screen, (6, 6), (18, 6))
        elif self.direction == 'down':
            self._set_pupil_pos(screen, (6, 11), (18, 11))
        elif self.direction == 'left':
            self._set_pupil_pos(screen, (4, 9), (16, 9))
        elif self.direction == 'right':
            self._set_pupil_pos(screen, (8, 9), (20, 9))

    def set_direction(self, direction):
        self.direction = direction
