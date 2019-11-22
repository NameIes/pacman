import pygame
#TODO: Переименовать класс покороче - DONE
#TODO: Переместить файл в папку, где у нас обычно лежат классы
class Grain:

	def __init__(self, center_x, center_y, radius = 2, color = (255, 255, 0)):
		self.center_x = center_x
		self.center_y = center_y
		self.radius = radius
		self.color = color

	def draw(self, screen):
		pygame.draw.circle(screen, self.color,(self.center_x, self.center_y), self.radius)


class Energizer(Grain):

	def __init__(self, center_x, center_y, radius = 2, color = (255, 255, 0)):
		super().__init__(center_x, center_y)
		self.radius = 7

	def draw(self, screen):
		pygame.draw.circle(screen, self.color,(self.center_x, self.center_y), self.radius)
