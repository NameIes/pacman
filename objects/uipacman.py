import math
from ready import Text
import pygame

yellow = 255, 255, 0


class ScoreLable:
    def __init__(self, center_x, center_y):
        self.value = 0
        self.font_size = 18
        self.text = Text("00", self.font_size)
        tsize = self.text.get_text_size()
        self.text.update_position(center_x - tsize[0] / 2,
                                  center_y - tsize[1] / 2)
        # так какое цифра все время растет но приведение этом растет
        # только влево
        self.truex = center_x + tsize[0] / 2
        self.truey = center_y + tsize[1] / 2

    def draw(self, screen):
        self.text.draw(screen)

    def update_value(self, value):
        self.value = value
        self.text = Text(str(self.value), self.font_size)
        tsize = self.text.get_text_size()
        self.text.update_position(self.truex - tsize[0], self.truey - tsize[1])


class Health:
    def __init__(self, x, y):
        self.start_value = 3
        self.value = self.start_value
        self.radius = int(12)
        self.x = int(x)
        self.y = int(y)

    def draw(self, screen):
        "Draw health"
        rang = list(range(210, 360)) + list(range(0, 150))
        center_x = self.x + self.radius
        center_y = self.y + self.radius

        for i in range(self.value):
            p = [(center_x, center_y)]
            for n in rang:
                x1 = int(center_x + self.radius * math.cos(n * math.pi / 180))
                y1 = int(center_y + self.radius * math.sin(n * math.pi / 180))
                p.append((x1, y1))
                # p.append((center_x, center_y))
            pygame.gfxdraw.filled_polygon(screen, p, yellow)
            center_x += 5 + 2 * self.radius

    def die(self):
        "Decrease health"
        self.value -= 1
        if self.value < 0:
            self.value = 0
