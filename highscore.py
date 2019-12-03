import array
import sys
import pygame

from objects.field import black
from ready import Text


def highscore_table(screen):
    with open('records.txt') as f: #чтение из файла. Файл пример
        data = list(map(int, f.read().split())) #чтение из файла
    data = sorted(data, reverse=True) #сортировка по возрастанию
    text_object1 = Text("Highscore", 50)
    text_object1.update_position(50, 10)
    text_object2 = Text('1.   ' + str(data[0]), 30)
    text_object2.update_position(10, 70)
    text_object3 = Text('2.   ' + str(data[1]), 30)
    text_object3.update_position(10, 100)
    text_object4 = Text('3.   ' + str(data[2]), 30)
    text_object4.update_position(10, 130)
    text_object5 = Text('4.   ' + str(data[3]), 30)
    text_object5.update_position(10, 160)
    text_object6 = Text('5.   ' + str(data[4]), 30)
    text_object6.update_position(10, 190)
    text_object7 = Text('6.   ' + str(data[5]), 30)
    text_object7.update_position(10, 220)
    text_object8 = Text('7.   ' + str(data[6]), 30)
    text_object8.update_position(10, 250)
    text_object9 = Text('8.   ' + str(data[7]), 30)
    text_object9.update_position(10, 280)
    text_object10 = Text('9.   ' + str(data[8]), 30)
    text_object10.update_position(10, 310)
    text_object11 = Text('10.  ' + str(data[9]), 30)
    text_object11.update_position(10, 340)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)
        text_object1.draw(screen)
        text_object2.draw(screen)
        text_object3.draw(screen)
        text_object4.draw(screen)
        text_object5.draw(screen)
        text_object6.draw(screen)
        text_object7.draw(screen)
        text_object8.draw(screen)
        text_object9.draw(screen)
        text_object10.draw(screen)
        text_object11.draw(screen)
        pygame.display.flip()
        pygame.time.wait(20)
        pygame.display.update()
    sys.exit(0)
