from ready import Text


class ScoreLable:
    def __init__(self, center_x, center_y):
        self.value = 0
        self.font_size = 14
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
