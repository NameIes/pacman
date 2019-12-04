def prepare_field(walls_id, field):
    t_maze = []
    for y in field:
        line = []
        for x in y:
            if x in walls_id:
                line.append(-1)
            else:
                line.append(0)
        t_maze.append(line)

    return t_maze


def push_wave(y, x, lvl, h, w, field, end, isf=False):
    field[y][x] = lvl

    if (y, x) == end:
        isf = True
    if isf:
        return field

    if x + 1 < w:
        if field[y][x + 1] == 0 or (field[y][x + 1] != -1 and field[y][x + 1] > lvl):
            push_wave(y, x + 1, lvl + 1, h, w, field, end, isf)
    if y + 1 < h:
        if field[y + 1][x] == 0 or (field[y + 1][x] != -1 and field[y + 1][x] > lvl):
            push_wave(y + 1, x, lvl + 1, h, w, field, end, isf)
    if y - 1 >= 0:
        if field[y - 1][x] == 0 or (field[y - 1][x] != -1 and field[y - 1][x] > lvl):
            push_wave(y - 1, x, lvl + 1, h, w, field, end, isf)
    if x - 1 >= 0:
        if field[y][x - 1] == 0 or (field[y][x - 1] != -1 and field[y][x - 1] > lvl):
            push_wave(y, x - 1, lvl + 1, h, w, field, end, isf)

    return field


def get_path(start, finish, field, h, w):
    if field[finish[0]][finish[1]] in [0, -1]:
        raise

    path = []
    item = finish
    while not path.append(item[::-1]) and item != start:
        r = (item[0] + 1, item[1])
        if r[0] < w and field[r[0]][r[1]] == field[item[0]][item[1]] - 1:
            item = r
            continue

        l = (item[0] - 1, item[1])
        if l[0] >= 0 and field[l[0]][l[1]] == field[item[0]][item[1]] - 1:
            item = l
            continue

        u = (item[0], item[1] - 1)
        if u[1] >= 0 and field[u[0]][u[1]] == field[item[0]][item[1]] - 1:
            item = u
            continue

        d = (item[0], item[1] + 1)
        if d[1] < h and field[d[0]][d[1]] == field[item[0]][item[1]] - 1:
            item = d
            continue

    return path[::-1]


def modify_path(path):
    if len(path) == 1:
        return path

    result = []
    t = 0 if path[0][0] != path[1][0] else 1
    for i in range(len(path) - 1):
        if (path[i][0] == path[i + 1][0] and path[i][1] != path[i + 1][1] and t == 0) or (
                path[i][1] == path[i + 1][1] and path[i][0] != path[i + 1][0] and t == 1):
            result.append(path[i])
            t = 1 if t == 0 else 0
    result.append(path[-1])

    return result
