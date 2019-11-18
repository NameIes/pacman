import pygame


class GhostBase:
    scared = 'res/img/scared.png'
    direction_speed = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}

    def __init__(self, x, y, direction='up', anim_speed=10, pacman_rect=None):
        self.pacman_rect = pacman_rect  # Будет нужно для ИИ движения

        self.images = None
        self.image = None
        self.rect = None

        self.anim_speed = anim_speed
        self.timer = 0
        self.anim_stage = True

        self.direction = direction
        self.scared = False
        self.is_death = False
        self.speed = GhostBase.direction_speed[direction]

    def process_logic(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if not self.scared or self.is_death:  # Анимация
            self.timer += 1
            if self.timer == self.anim_speed:
                self.image = self.images[1 if self.anim_stage else 0]

                self.anim_stage = not self.anim_stage
                self.timer = 0
        elif self.scared:  # Напуган, когда съедено большое зерно
            self.image = pygame.image.load(GhostBase.scared)

    def process_draw(self, screen):
        # Когда съеден пакманом, на базу бегут только глаза
        if not self.is_death:
            screen.blit(self.image, self.rect)

        if self.scared:
            return

        # Глаза
        pygame.draw.ellipse(screen, (255, 255, 255), (self.rect[0] + 4, self.rect[1] + 6, 8, 10))
        pygame.draw.ellipse(screen, (255, 255, 255), (self.rect[0] + 16, self.rect[1] + 6, 8, 10))

        # Зрачки поворачиваются в сторону движения
        if self.direction == 'up':
            pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + 6, self.rect[1] + 6, 4, 5))
            pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + 18, self.rect[1] + 6, 4, 5))
        elif self.direction == 'down':
            pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + 6, self.rect[1] + 11, 4, 5))
            pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + 18, self.rect[1] + 11, 4, 5))
        elif self.direction == 'left':
            pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + 4, self.rect[1] + 9, 4, 5))
            pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + 16, self.rect[1] + 9, 4, 5))
        elif self.direction == 'right':
            pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + 8, self.rect[1] + 9, 4, 5))
            pygame.draw.rect(screen, (22, 0, 255), (self.rect[0] + 20, self.rect[1] + 9, 4, 5))

    def set_direction(self, direction):
        self.direction = direction
        self.speed = GhostBase.direction_speed[direction]
