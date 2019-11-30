import pygame
import random
from objects.field import pole_xy, get_pos_in_field, is_cell_centre
from objects.lee_pathfinder import *


class GhostBase:
    scared = 'res/img/scared.png'

    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None, speed=1):
        self.direction_vector = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}

        self.pacman_rect = pacman_rect  # Будет нужно для ИИ движения

        self.images = None
        self.image = None
        self.rect = None

        self.anim_speed = anim_speed
        self.timer = 0
        self.anim_stage = True

        self.direction = direction
        self.direction_speed = self.direction_vector.copy()
        self.set_speed(speed)

        self.is_killed = False
        self._is_dead = False
        self.is_dead_process = False
        self.is_dead_path = []

        self.scared = False
        self.scared_time = 500
        self.scared_timer = 0

    def set_speed(self, speed):
        for item in self.direction_speed:
            if self.direction_speed[item][0] != 0:
                self.direction_speed[item][0] = speed if self.direction_speed[item][0] > 0 else -speed
            if self.direction_speed[item][1] != 0:
                self.direction_speed[item][1] = speed if self.direction_speed[item][1] > 0 else -speed

    def scared_move(self):
        # TODO: Реализовать движение при испуге
        pass

    def _find_path(self):
        # Делаем копию поля, где стены -1, а дорожки 0
        m_field = prepare_field([1, 2], pole_xy.copy())

        # Получаем конечную точку
        spawn_points = [(17, 12), (17, 13), (17, 14), (17, 15)]
        r_point = spawn_points[random.randint(0, 3)]

        # Распространяем волну алгоритма Ли
        x, y = get_pos_in_field(self.rect.centerx, self.rect.centery)
        m_field = push_wave(y, x, 1, len(pole_xy), len(pole_xy[0]), m_field, r_point)

        # Восстанавливаем путь
        self.is_dead_path = get_path((y, x), r_point, m_field, len(m_field), len(m_field[0]))
        self.is_dead_path = modify_path(self.is_dead_path)

    def _push(self):
        # Двигает привидение после поворота, из-за того что даже is_cell_centre срабатывает несколько раз
        if self.direction == 'up':
            self.rect.y -= 2
        if self.direction == 'down':
            self.rect.y += 2
        if self.direction == 'left':
            self.rect.x -= 2
        if self.direction == 'right':
            self.rect.x += 2

    def _set_death_direction(self):
        # Проверяем вернулся ли призрак в клетку
        if len(self.is_dead_path) == 0:
            self.is_dead_process = False
            self._is_dead = False
            self.is_killed = False
            self.scared = False
            self.set_speed(1)
            return

        # Устанавливаем нужное направление в зависимости от координаты
        x, y = get_pos_in_field(self.rect.centerx, self.rect.centery)
        if y < self.is_dead_path[0][1]:
            self.direction = 'down'
        if y > self.is_dead_path[0][1]:
            self.direction = 'up'
        if x < self.is_dead_path[0][0]:
            self.direction = 'right'
        if x > self.is_dead_path[0][0]:
            self.direction = 'left'

    def death_move(self):
        # Вызываем функцию поиска пути один раз
        if not self.is_dead_process:
            self.set_speed(2)
            self._find_path()
            self._set_death_direction()
            self.is_dead_process = True

        # Проверяем достиг ли призрак нужной точки
        x, y = get_pos_in_field(self.rect.centerx, self.rect.centery)
        if (x, y) == self.is_dead_path[0]:
            if is_cell_centre(self.rect.centerx, self.rect.centery):
                self.is_dead_path.pop(0)
                self._set_death_direction()
                self._push()

    def kill(self):
        self.is_killed = True

    def escape_move(self):
        x, y = get_pos_in_field(self.rect.centerx, self.rect.centery)

        if x not in [13, 14] and is_cell_centre(self.rect.centerx, self.rect.centery):
            self.direction = 'left' if x > 13 else 'right'
        elif x in [13, 14] and is_cell_centre(self.rect.centerx, self.rect.centery):
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

        return p_dirs[random.randint(0, len(p_dirs) - 1)]

    def process_logic(self):
        self.rect.x += self.direction_speed[self.direction][0]
        self.rect.y += self.direction_speed[self.direction][1]

        if self.is_killed and is_cell_centre(self.rect.centerx, self.rect.centery):
            self._is_dead = True
        if self._is_dead:
            self.death_move()
            return

        self.image_controller()

        x, y = get_pos_in_field(self.rect.centerx, self.rect.centery)
        if pole_xy[y][x] == 4:
            self.escape_move()
            return

        if self.scared:
            self.scared_timer += 1
            if self.scared_timer == self.scared_time:
                self.scared = False
                self.scared_timer = 0

        # OLD ALGORITHM =====================================================
        if y == 17:
            if x == 0:
                self.direction = 'right'
            if x == 27:
                self.direction = 'left'
        if pole_xy[y][x] == 3:
            if is_cell_centre(self.rect.centerx, self.rect.centery):
                self.direction = self.get_rand_direction(x, y)

                self._push()
        # ===================================================================

    def _set_pupil_pos(self, screen, left, right):
        pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + left[0], self.rect[1] + left[1], 4, 5))
        pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + right[0], self.rect[1] + right[1], 4, 5))

    def image_controller(self):
        if not self.scared or self._is_dead:  # Анимация
            self.timer += 1
            if self.timer == self.anim_speed:
                self.image = self.images[1 if self.anim_stage else 0]

                self.anim_stage = not self.anim_stage
                self.timer = 0
        elif self.scared:  # Напуган, когда съедено большое зерно
            self.image = pygame.image.load(GhostBase.scared)

    def process_draw(self, screen):
        # Когда съеден пакманом, на базу бегут только глаза
        if not self._is_dead:
            screen.blit(self.image, self.rect)

        if self.scared and not self._is_dead:
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
