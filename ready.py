import sys, pygame


class Text:
    def __init__(self, data, size, x=0, y=0, color=(255, 255, 255)):
        self.position = (x, y)
        self.data = data
        self.size = size
        self.color = color
        self.font = pygame.font.Font('crackman.ttf', self.size)
        self.surface = self.font.render(self.data, True, self.color)

    def update_position(self, x, y):
        self.position = (x, y)

    def update_text(self, text):
        self.data = str(text)
        self.surface = self.font.render(self.data, True, self.color)

    def get_text_size(self):
        r = self.surface.get_rect()
        return [r.width, r.height]

    def draw(self, screen):
        screen.blit(self.surface, self.position)


def ready():
    size = (800, 600)
    black = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode(size)

    game_over = False

    display_text_until = pygame.time.get_ticks() + 3000
    text_object = Text("READY", 90)
    text_size = text_object.get_text_size()
    text_object.update_position(size[0] / 2 - text_size[0] / 2, size[1] / 2 - text_size[1] / 2)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)

        if pygame.time.get_ticks() < display_text_until:
            text_object.draw(screen)
# TODO добавить вызов функции "основной игры"

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    ready()
