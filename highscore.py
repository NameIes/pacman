import sys
import pygame

from objects.field import black
from ready import Text

def highscore_table(screen):
    text_object1 = Text("Highscore", 50)
    text_object1.update_position(50, 10)
    text_object2 = Text('1.', 30)
    text_object2.update_position(10, 70)
    text_object3 = Text('2.', 30)
    text_object3.update_position(10, 100)
    text_object4 = Text('3.', 30)
    text_object4.update_position(10, 130)
    text_object5 = Text('4.', 30)
    text_object5.update_position(10, 160)
    text_object6 = Text('5.', 30)
    text_object6.update_position(10, 190)
    text_object7 = Text('6.', 30)
    text_object7.update_position(10, 220)
    text_object8 = Text('7.', 30)
    text_object8.update_position(10, 250)
    text_object9 = Text('8.', 30)
    text_object9.update_position(10, 280)
    text_object10 = Text('9.', 30)
    text_object10.update_position(10, 310)
    text_object11 = Text('10.', 30)
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
