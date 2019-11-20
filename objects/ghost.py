import pygame


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

    def death_move(self):
        # TODO: Реализовать движение на спавн после смерти
        pass

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
        # TODO: Реализовать алгоритм движения по коридорам ()

        self.rect.x += self.direction_speed[self.direction][0]
        self.rect.y += self.direction_speed[self.direction][1]

        self.image_controller()

    def _set_pupil_pos(self, screen, left, right):
        pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + left[0], self.rect[1] + left[1], 4, 5))
        pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + right[0], self.rect[1] + right[1], 4, 5))

    def process_draw(self, screen):
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
