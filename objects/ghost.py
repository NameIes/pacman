import pygame
from random import randint
from objects.field import pole_xy, get_pos_in_field, is_cell_centre
from objects.lee_pathfinder import *
from copy import deepcopy


class GhostBase:
    images = {
        'scared': pygame.image.load('res/img/scared.png'),
        'blinky': [pygame.image.load('res/img/blinky_0.png'),
                   pygame.image.load('res/img/blinky_1.png')],
        'clyde': [pygame.image.load('res/img/clyde_0.png'),
                  pygame.image.load('res/img/clyde_1.png')],
        'inky': [pygame.image.load('res/img/inky_0.png'),
                 pygame.image.load('res/img/inky_1.png')],
        'pinky': [pygame.image.load('res/img/pinky_0.png'),
                  pygame.image.load('res/img/pinky_1.png')]
    }
    direction_vector = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}

    def __init__(self, x, y, ghost_name, pacman_obj=None, move_speed=1, anim_speed=10, direction='up'):
        self.pacman_obj = pacman_obj

        self.images = GhostBase.images[ghost_name]
        self.current_image = self.images[0]
        self.rect = self.current_image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.in_field_x = None
        self.in_field_y = None

        self.anim_speed = anim_speed
        self.anim_timer = 0
        self.anim_stage = True

        self.direction = direction
        self.direction_speed = deepcopy(GhostBase.direction_vector)
        self.set_move_speed(move_speed)

        self.is_dead = False
        self.is_dead_process = False
        self.is_dead_path = []

        self.scared = False
        self.scared_time = 500
        self.scared_timer = 0

    def set_move_speed(self, speed):
        self.direction_speed = deepcopy(GhostBase.direction_vector)
        for item in self.direction_speed:
            self.direction_speed[item][0] *= speed
            self.direction_speed[item][1] *= speed

    def scared_move(self):
        # TODO: Реализовать движение при испуге
        pass

    def _find_path(self):
        # Делаем копию поля, где стены -1, а дорожки 0
        prepared_field = prepare_field([1, 2], pole_xy.copy())

        # Получаем конечную точку
        spawn_points = [(17, 12), (17, 13), (17, 14), (17, 15)]
        end_point = spawn_points[randint(0, 3)]

        # Распространяем волну алгоритма Ли
        prepared_field = push_wave(self.in_field_y, self.in_field_x, 1, len(pole_xy), len(pole_xy[0]), prepared_field,
                                   end_point)

        # Восстанавливаем путь
        self.is_dead_path = get_path((self.in_field_y, self.in_field_x), end_point, prepared_field,
                                     len(prepared_field[0]), len(prepared_field))
        self.is_dead_path = modify_path(self.is_dead_path)

    def _push_towards(self):
        # Двигает привидение в сторону движения, иначе привидения поворачивает несколько раз в одной развилке
        if self.direction == 'up':
            self.rect.y -= 2
        if self.direction == 'down':
            self.rect.y += 2
        if self.direction == 'left':
            self.rect.x -= 2
        if self.direction == 'right':
            self.rect.x += 2

    def _set_death_direction(self):
        # Устанавливаем нужное направление в зависимости от координаты
        if self.in_field_y < self.is_dead_path[0][1]:
            self.direction = 'down'
        if self.in_field_y > self.is_dead_path[0][1]:
            self.direction = 'up'
        if self.in_field_x < self.is_dead_path[0][0]:
            self.direction = 'right'
        if self.in_field_x > self.is_dead_path[0][0]:
            self.direction = 'left'

    def death_move(self):
        # Вызываем функцию поиска пути один раз
        if not self.is_dead_process:
            self.set_move_speed(2)
            self._find_path()
            self._set_death_direction()
            self.is_dead_process = True

        # Проверяем достиг ли призрак нужной точки
        if (self.in_field_x, self.in_field_y) == self.is_dead_path[0]:
            if is_cell_centre(self.rect.centerx, self.rect.centery):
                self.is_dead_path.pop(0)

                # Проверяем вернулся ли призрак в клетку
                if len(self.is_dead_path) == 0:
                    self.is_dead_process = False
                    self.is_dead = False
                    self.scared = False
                    self.set_move_speed(1)
                    return

                self._set_death_direction()
                self._push_towards()

    def kill(self):
        self.is_dead = True

    def escape_move(self):
        if self.in_field_x not in [13, 14] and is_cell_centre(self.rect.centerx, self.rect.centery):
            self.direction = 'left' if self.in_field_x > 13 else 'right'
        elif self.in_field_x in [13, 14] and is_cell_centre(self.rect.centerx, self.rect.centery):
            self.direction = 'up'

    def get_rand_direction(self, x, y):
        p_dirs = []

        if pole_xy[y - 1][x] not in [1, 4] and self.direction != 'down':
            p_dirs.append('up')
        if pole_xy[y][x - 1] not in [1, 4] and self.direction != 'right':
            p_dirs.append('left')
        if pole_xy[y + 1][x] not in [1, 4] and self.direction != 'up':
            p_dirs.append('down')
        if pole_xy[y][x + 1] not in [1, 4] and self.direction != 'left':
            p_dirs.append('right')

        return p_dirs[randint(0, len(p_dirs) - 1)]

    def process_logic(self):
        # Узнаем позицию в поле
        self.in_field_x, self.in_field_y = get_pos_in_field(self.rect.centerx, self.rect.centery)

        # Движение в направлении
        self.rect.x += self.direction_speed[self.direction][0]
        self.rect.y += self.direction_speed[self.direction][1]

        # Возращение в клетку после смерти
        if self.is_dead and is_cell_centre(self.rect.centerx, self.rect.centery):
            self.death_move()
            return

        # Адекватный выход из клетки
        if pole_xy[self.in_field_y][self.in_field_x] == 4:
            self.escape_move()
            return

        # Режим паники
        if self.scared:
            self.scared_timer += 1
            if self.scared_timer == self.scared_time:
                self.scared = False
                self.scared_timer = 0

        # Алгоритм поведения привидений
        # OLD ALGORITHM =====================================================
        if self.in_field_y == 17:
            if self.in_field_x == 0:
                self.direction = 'right'
            if self.in_field_x == 27:
                self.direction = 'left'
        if pole_xy[self.in_field_y][self.in_field_x] == 3:
            if is_cell_centre(self.rect.centerx, self.rect.centery):
                self.direction = self.get_rand_direction(self.in_field_x, self.in_field_y)

                self._push_towards()
        # ===================================================================

    def _set_pupil_pos(self, screen, left, right):
        pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + left[0], self.rect[1] + left[1], 4, 5))
        pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + right[0], self.rect[1] + right[1], 4, 5))

    def image_controller(self):
        if not self.scared or self.is_dead:  # Анимация
            self.anim_timer += 1
            if self.anim_timer == self.anim_speed:
                self.current_image = self.images[1 if self.anim_stage else 0]

                self.anim_stage = not self.anim_stage
                self.anim_timer = 0
        elif self.scared:  # Напуган, когда съедено большое зерно
            self.current_image = GhostBase.images['scared']

    def process_draw(self, screen):
        # Когда съеден пакманом, в клетку бегут только глаза
        if not self.is_dead:
            screen.blit(self.current_image, self.rect)
            self.image_controller()

        # Режим паники
        if self.scared and not self.is_dead:
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
