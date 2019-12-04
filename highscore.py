# -*- coding: utf-8 -*-
import sys
import pygame

from objects.field import black
from ready import Text
from functools import reduce


class HighscoreTable:
    def __init__(self, ):
        # TODO: проверка существования файла
        with open('records.txt') as f:
            data = list(map(int, f.read().split()))
        self.data = sorted(data, reverse=True)
        self.x = 50
        self.y = 10
        self.fsize = 50
        self.text_array = []
        txt_obj0 = Text("Highscore", self.fsize)
        txt_obj0.update_position(self.x, self.y)
        self.y += 20
        self.text_array.append(txt_obj0)
        for i in range(10):
            if i < len(data):
                s = str(data[i])
            else:
                s = " -- "
            self.text_array.append(Text(str(i + 1) + '.   ' + s,
                                        self.fsize-20))
            self.text_array[i + 1].update_position(
                self.x, self.y + (i + 1) * (self.fsize - 10))

        self.max_score = 0
        if len(data) > 0:
            self.max_score = data[0]

    def draw(self, screen):
        for i in self.text_array:
            i.draw(screen)

    def add_new_score(self, score):
        score_added = False
        if len(self.data) < 10:
            score_added = True
            self.data.append(int(score))
        else:
            lower_then = [x < score for x in self.data]
            score_added = reduce(lambda x, y: x or y, lower_then)
            self.data[-1] = int(score)

        if score_added:
            self.data = sorted(self.data, reverse=True)
            for i in range(10):
                if i < len(self.data):
                    s = str(self.data[i])
                else:
                    s = " -- "
                self.text_array[i+1].update_text(str(i + 1) + '.   ' + s)

            self.max_score = self.data[0]
            print("Write new score into table_score")
            with open('records.txt', 'w') as f:
                for i in self.data:
                    f.write(str(i)+' ')


def highscore_table(screen):
    table_score = HighscoreTable()

    game_over = False
    game_quit = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == 'q':
                    game_over = True
                    # main_menu(screen, game, highscore_table)

        screen.fill(black)
        table_score.draw(screen)

        pygame.display.flip()
        pygame.time.wait(20)
        pygame.display.update()
    if game_quit:
        sys.exit(0)
