import pygame, sys

z = int(14)
# z равна половине ширины коридора между стенами
# Размер Pacman и привидений = 2 * z
# size = width, height = определяется как размер загруженного поля
# Размеры поля могут быть изменяемы в зависимости от того какое поле загружено (размеры матрицы поля -1)
black = 0, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
red = 255, 0, 0
yellow = 255, 255, 153

# 2 - Поле для очков и другой информации
# 0 , 3 - Ячейки по которым могут ходить "Герои"
# 3 - Ячейки, в которых возможны повороты
# 1 - Ячейки, на которых расположены "Стены"
# Реализован промежуточный вариант отображения поля, цветом выделены пути, по которым могут ходить
# Центр фигур должен ходить по центру показанных дорожек
# Правильное отображение поле будет позднее
# матрицу pole_xy можно использовать для размещения фигур на поле
# Если pole_xy[i][j] == 0, то в эту ячейку можно поместить зерно , Pacman , Привидений.
# Координата центра ячейки (j * z + z// 2; i * z + z // 2) ---!!! НЕ ВЕРНО - центр 4 точки
# Координаты для размещения фигур:
# Если помещаем фигуру и ее центр должен совпадать с центром клеточки,
# ее координаты должна быть:
# если круг, то центр круга - ((j * z  + z // 2; i * z + z // 2)
# Если фигура прямоугольник, (x , y - ширина, высота )
# то координаты ее левого верхнего угла должны быть
# Координаты:  (j * z  + (z-x)// 2; i * z + (z-y) // 2)

pole_xy = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 1, 1, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 3, 0, 0, 0, 0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0, 0, 0, 0, 3, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 3, 0, 3, 1, 1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1, 1, 3, 0, 3, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
           [1, 3, 0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0, 3, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
           ]

SIZE = width, height = z * len(pole_xy[0]), z * len(pole_xy)


def show_field(screen, field=pole_xy, color_f=(0, 0, 255)):
    for yy in range((len(pole_xy))):
        for xx in range(len(pole_xy[yy])):
            if int(pole_xy[yy][xx]) == 0:
                pygame.draw.rect(screen, color_f, (z * xx, z * yy, z, z), 0)
            elif int(pole_xy[yy][xx]) == 3:
                pygame.draw.rect(screen, color_f, (z * xx, z * yy, z, z), 0)
            else:
                pass
