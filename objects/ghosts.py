from objects.ghost import GhostBase
from objects.field import get_pos_in_field
from copy import deepcopy


class Blinky(GhostBase):
    def __init__(self, x, y, pacman_obj, move_speed=0, anim_speed=10, direction='up'):
        super().__init__(x, y, 'blinky', pacman_obj, move_speed, anim_speed, direction)
        self.start_after = 1

    def calc_vectors(self, possible_directions):
        vectors = []
        for dirs in possible_directions:
            gx, gy = self.in_field_x, self.in_field_y
            px, py = get_pos_in_field(self.pacman_obj.x, self.pacman_obj.y)
            if dirs == 'left':
                gx -= 1
            if dirs == 'right':
                gx += 1
            if dirs == 'up':
                gy -= 1
            if dirs == 'down':
                gy += 1

            vectors.append(int(((gx - px)**2 + (gy - py)**2)**0.5))

        return vectors


class Pinky(GhostBase):
    def __init__(self, x, y, pacman_obj, move_speed=0, anim_speed=10, direction='up'):
        super().__init__(x, y, 'pinky', pacman_obj, move_speed, anim_speed, direction)
        self.start_after = 1

    def calc_vectors(self, possible_directions):
        vectors = []
        for dirs in possible_directions:
            gx, gy = self.in_field_x, self.in_field_y
            px, py = get_pos_in_field(self.pacman_obj.x, self.pacman_obj.y)

            if self.pacman_obj.direction == 'w':
                py -= 4
            if self.pacman_obj.direction == 'a':
                px -= 4
            if self.pacman_obj.direction == 's':
                py += 4
            if self.pacman_obj.direction == 'd':
                px += 4

            if dirs == 'left':
                gx -= 1
            if dirs == 'right':
                gx += 1
            if dirs == 'up':
                gy -= 1
            if dirs == 'down':
                gy += 1

            vectors.append(int(((gx - px)**2 + (gy - py)**2)**0.5))

        return vectors


class Inky(GhostBase):
    def __init__(self, x, y, pacman_obj, blinky_obj, move_speed=0, anim_speed=10, direction='up'):
        super().__init__(x, y, 'inky', pacman_obj, move_speed, anim_speed, direction)

        self.blinky_obj = blinky_obj
        self.start_after = 30

    def calc_vectors(self, possible_directions):
        vectors = []
        for dirs in possible_directions:
            gx, gy = deepcopy(self.blinky_obj.in_field_x), deepcopy(self.blinky_obj.in_field_y)
            px, py = get_pos_in_field(self.pacman_obj.x, self.pacman_obj.y)

            if self.pacman_obj.direction == 'w':
                py -= 2
            if self.pacman_obj.direction == 'a':
                px -= 2
            if self.pacman_obj.direction == 's':
                py += 2
            if self.pacman_obj.direction == 'd':
                px += 2

            if dirs == 'left':
                gx -= 1
            if dirs == 'right':
                gx += 1
            if dirs == 'up':
                gy -= 1
            if dirs == 'down':
                gy += 1

            vectors.append(int(((gx - px)**2 + (gy - py)**2)**0.5) * 2)

        return vectors


class Clyde(GhostBase):
    def __init__(self, x, y, pacman_obj, move_speed=0, anim_speed=10, direction='up'):
        super().__init__(x, y, 'clyde', pacman_obj, move_speed, anim_speed, direction)

        self.start_after = 100

    def calc_vectors(self, possible_directions):
        vectors = []
        for dirs in possible_directions:
            gx, gy = self.in_field_x, self.in_field_y
            px, py = get_pos_in_field(self.pacman_obj.x, self.pacman_obj.y)
            if dirs == 'left':
                gx -= 1
            if dirs == 'right':
                gx += 1
            if dirs == 'up':
                gy -= 1
            if dirs == 'down':
                gy += 1

            vector = int(((gx - px) ** 2 + (gy - py) ** 2) ** 0.5)

            if vector < 8:
                vectors.append(vector)
            else:
                vectors.append(int(((gx - 1) ** 2 + (gy - 35) ** 2) ** 0.5))

        return vectors
