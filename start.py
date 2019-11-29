# -*- coding: utf-8 -*-

import sys

import pause
from objects.ghosts import *
from objects.field import FIELD_SIZE, pole_xy, show_field
from pause import paused
from ready import Text


def main():
	size = FIELD_SIZE
	black = (0, 0, 0)

	pygame.init()
	screen = pygame.display.set_mode(size)

	# Пример
	# TODO: подставлять координаты спавна приведений из нашего уровня
	lst = [
		Blinky(10, 10, direction='right'),
		Pinky(750, 10, direction='down'),
		Inky(750, 550, direction='left'),
		Clyde(10, 550, direction='up'),
		Blinky(300, 200, direction='right'),
		Blinky(500, 400, direction='left')
	]
	lst[-2].scared = True
	lst[-1].is_death = True
	#

	game_over = False

	pause_flag = False
	text_pause = Text("PAUSE", 100)
	text_pause_size = text_pause.get_text_size()
	text_pause.update_position(size[0] / 2 - text_pause_size[0] / 2, size[1] / 2 - text_pause_size[1] / 2)

	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			elif event.type == pygame.KEYDOWN:
				if chr(event.key) == 'p':
					paused()

		screen.fill(black)

		show_field(screen, pole_xy, (0, 0, 127))
		# Пример
		for i in lst:
			i.process_logic()
			i.process_draw(screen)

		if pause_flag:
			text_pause.draw(screen)

		pygame.display.flip()
		pygame.time.wait(10)

	sys.exit(0)


if __name__ == '__main__':
	main()
