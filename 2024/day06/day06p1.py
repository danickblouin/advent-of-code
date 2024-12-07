lines = [line.rstrip() for line in open('input.txt').readlines()]

lines = [list(line) for line in lines]


def get_guard_pos():
    for row in range(len(lines)):
        for col in range(len(lines)):
            if lines[row][col] == '^':
                return [row, col], 'up'
            elif lines[row][col] == 'v':
                return [row, col], 'down'
            elif lines[row][col] == '>':
                return [row, col], 'right'
            elif lines[row][col] == '<':
                return [row, col], 'left'


def check_obstacle(guard_pos):
    row, col = guard_pos[0][0], guard_pos[0][1]
    if guard_pos[1] == 'up' and (row + 1 < len(lines)) and lines[row - 1][col] == '#':
        return True
    if guard_pos[1] == 'down' and (row + 1 < len(lines)) and lines[row + 1][col] == '#':
        return True
    if guard_pos[1] == 'right' and (col + 1 < len(lines)) and lines[row][col + 1] == '#':
        return True
    if guard_pos[1] == 'left' and (col + 1 < len(lines)) and lines[row][col - 1] == '#':
        return True


def check_out(guard_pos):
    row, col = guard_pos[0][0], guard_pos[0][1]
    if row == 0 or row == len(lines) - 1 or col == 0 or col == len(lines) - 1:
        return True


total = 0

while True:
    pos = get_guard_pos()
    row, col = pos[0][0], pos[0][1]
    if pos[1] == 'up':
        lines[row - 1][col] = '^'
        lines[row][col] = 'X'
        total += 1
    elif pos[1] == 'down':
        lines[row + 1][col] = 'v'
        lines[row][col] = 'X'
        total += 1
    elif pos[1] == 'right':
        lines[row][col + 1] = '>'
        lines[row][col] = 'X'
        total += 1
    elif pos[1] == 'left':
        lines[row][col - 1] = '<'
        lines[row][col] = 'X'
        total += 1

    pos = get_guard_pos()
    row, col = pos[0][0], pos[0][1]
    if check_obstacle(pos):
        if pos[1] == 'up':
            lines[row][col] = '>'
        elif pos[1] == 'down':
            lines[row][col] = '<'
        elif pos[1] == 'right':
            lines[row][col] = 'v'
        elif pos[1] == 'left':
            lines[row][col] = '^'

    pos = get_guard_pos()

    if row == 0 or row == len(lines) - 1 or col == 0 or col == len(lines) - 1:
        break


pos = get_guard_pos()


total = 1
for line in lines:
    total += line.count('X')

print(total)
