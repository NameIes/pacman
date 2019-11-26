import pygame, sys

blue = 0, 255, 0
black = 0, 0, 0


# a , b - координаты прямоугольника, w, h - ширина и высота, z - множитель, r - скругление углов, в пикселях
def rect_1(screen, a=int(0), b=int(0), w=100, h=200, r=5, d =1, z=1 ):
    pygame.draw.lines(screen, blue, True, [[a + r, b], [a + w * z - r, b],
                                           [a + w * z, b + r], [a + w * z, b + h * z - r],
                                           [a + w * z - r, b + h * z], [a + r, b + h * z], [a, b + h * z - r],
                                           [a, b + r]], d)


def fig_1(screen, a=int(0), b=int(0), w=100, h=200, m=40, r=5, z=1):
    pygame.draw.lines(screen, blue, True,
                      [[a + r, b], [a + w * z - r, b], [a + w * z, b + r], [a + w * z, b + m * z - r],
                       [a + w * z - r, b + m * z], [a + w // 2 * z + m // 2 * z + r, b + m * z],
                       [a + w * z // 2 + m // 2 * z, b + m * z + r], [a + w * z // 2 + m // 2 * z, b + h * z - r],
                       [a + w * z // 2 + m // 2 * z - r, b + h * z], [a + w * z // 2 - m * z // 2 + r, b + h * z],
                       [a + w * z // 2 - m * z // 2, b + h * z - r], [a + w * z // 2 - m * z // 2, b + m * z + 6],
                       [a + w * z // 2 - m * z // 2 - r, b + m * z], [a + r, b + m * z], [a, b + m * z - r], [a, b + r]]
                      , 3)


def fig_2(screen, a=int(0), b=int(0), w=100, h=200, m=40, r=5, z=1):
    pygame.draw.lines(screen, blue, True,
                      [[a + w // 2 * z - m // 2 + r, b], [a + w // 2 * z + m // 2 - r, b],
                       [a + w // 2 * z + m // 2, b + r], [a + w // 2 * z + m // 2, b + h * z - m * z - r],
                       [a + w // 2 * z + m // 2 + r, b + h * z - m * z], [a + w * z - r, b + h * z - m * z],
                       [a + w * z, b + h * z - m * z + r], [a + w * z, b + h * z - r], [a + w * z - r, b + h * z],
                       [a + r, b + h * z], [a, b + h * z - r], [a, b + h * z - m * z + r], [a + r, b + h * z - m * z],
                       [a + w // 2 * z - m // 2 - r, b + h * z - m * z],
                       [a + w // 2 * z - m // 2, b + h * z - m * z - r], [a + w // 2 * z - m // 2, b + r]]
                      , 3)


def fig_2_2(screen, a=int(0), b=int(0), w=100, w1=50, h=200, m=40, r=5, z=1):
    pygame.draw.lines(screen, blue, True,
                      [[a + w1 * z - m // 2 + r, b], [a + w1 * z + m // 2 - r, b], [a + w1 * z + m // 2, b + r],
                       [a + w1 * z + m // 2, b + h * z - m * z - r], [a + w1 * z + m // 2 + r, b + h * z - m * z],
                       [a + w * z - r, b + h * z - m * z], [a + w * z, b + h * z - m * z + r],
                       [a + w * z, b + h * z - r], [a + w * z - r, b + h * z], [a + r, b + h * z], [a, b + h * z - r],
                       [a, b + h * z - m * z + r], [a + r, b + h * z - m * z],
                       [a + w1 * z - m // 2 - r, b + h * z - m * z], [a + w1 * z - m // 2, b + h * z - m * z - r],
                       [a + w1 * z - m // 2, b + r]]
                      , 3)


def fig_3(screen, a=int(0), b=int(0), w=100, h=200, m=40, r=5, z=1):
    pygame.draw.lines(screen, blue, True,
                      [[a + r, b], [a + m * z - r, b], [a + m * z, b + r], [a + m * z, b + h // 2 * z - m // 2 * z - r],
                       [a + m * z + r, b + h // 2 * z - m // 2 * z], [a + w * z - r, b + h // 2 * z - m // 2 * z],
                       [a + w * z, b + h // 2 * z - m // 2 * z + r], [a + w * z, b + h // 2 * z + m // 2 * z - r],
                       [a + w * z - r, b + h // 2 * z + m // 2 * z], [a + m * z + r, b + h // 2 * z + m // 2 * z],
                       [a + m * z, b + h // 2 * z + m // 2 * z + r], [a + m * z, b + h * z - r],
                       [a + m * z - r, b + h * z], [a + r, b + h * z], [a, b + h * z - r], [a, b + r]]
                      , 3)


def fig_4(screen, a=int(0), b=int(0), w=100, h=200, m=40, r=5, z=1):
    pygame.draw.lines(screen, blue, True,
                      [[a + r, b + h // 2 * z - m // 2 * z], [a + w * z - m * z - r, b + h // 2 * z - m // 2 * z],
                       [a + w * z - m * z, b + h // 2 * z - m // 2 * z - r], [a + w * z - m * z, b + r],
                       [a + w * z - m * z + r, b], [a + w * z - r, b], [a + w * z, b + r], [a + w * z, b + h * z - r],
                       [a + w * z - r, b + h * z], [a + w * z - m * z + r, b + h * z],
                       [a + w * z - m * z, b + h * z - r], [a + w * z - m * z, b + h // 2 * z + m // 2 * z + r],
                       [a + w * z - m * z - r, b + h // 2 * z + m // 2 * z], [a + r, b + h // 2 * z + m // 2 * z],
                       [a, b + h // 2 * z + m // 2 * z - r], [a, b + h // 2 * z - m // 2 * z + r]]
                      , 3)


def fig_5(screen, a=int(0), b=int(0), w=100, h=200, m=40, r=5, z=1):
    pygame.draw.lines(screen, blue, True,
                      [[a + r, b], [a + w * z - r, b], [a + w * z, b + r], [a + w * z, b + h * z - r],
                       [a + w * z - r, b + h * z], [a + w * z - m * z + r, b + h * z],
                       [a + w * z - m * z, b + h * z - r], [a + w * z - m * z, b + m * z + r],
                       [a + w * z - m * z - r, b + m * z], [a + r, b + m * z], [a, b + m * z - r], [a, b + r]]
                      , 3)


def fig_6(screen, a=int(0), b=int(0), w=100, h=200, m=40, r=5, z=1):
    pygame.draw.lines(screen, blue, True,
                      [[a+r,b],[a+w*z-r,b],[a+w*z,b+r],[a+w*z,b+m*z-r],[a+w*z-r,b+m*z],[a+m*z+r,b+m*z],[a+m*z,b+m*z+r],[a+m*z,b+h*z-r],[a+m*z-r,b+h*z],[a+r,b+h*z],[a,b+h*z-r],[a,b+r]]
                      , 3)


def draw_walls():
    pygame.init()
    size = width, height = 600, 800
    screen = pygame.display.set_mode(size)
    rect_1(screen, 30, 50)
    gameover = False

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        screen.fill(black)
        # rect_1(screen, 30, 50)
        # rect_1(screen, 130, 50, 300, 200, 5, 2)
        # fig_1(screen, 20, 30, 300, 200, 50, 5, 1)
        # fig_2(screen, 20, 130, 300, 200, 50, 5, 1)
        # fig_2_2(screen, 100, 130, 300,200, 200, 50, 5, 1)
        fig_6(screen, 20, 130, 300, 200, 50, 5, 1)
        # show_field(screen, pole_xy, (0, 0, 127))
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    draw_walls()
