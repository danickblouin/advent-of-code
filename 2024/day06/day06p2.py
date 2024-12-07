lines = [line.rstrip() for line in open('test.txt').readlines()]

lines = [list(line) for line in lines]


def get_guard_pos():
    for row in range(len(lines)):
        for col in range(len(lines[row])):
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
    if row >= len(lines) - 1 or col >= len(lines[row]) - 1:
        return False
    if guard_pos[1] == 'up' and lines[row - 1][col] == '#':
        return True
    if guard_pos[1] == 'down' and lines[row + 1][col] == '#':
        return True
    if guard_pos[1] == 'right' and lines[row][col + 1] == '#':
        return True
    if guard_pos[1] == 'left' and lines[row][col - 1] == '#':
        return True


def check_out(guard_pos):
    row, col = guard_pos[0][0], guard_pos[0][1]
    if row == 0 or row == len(lines) - 1 or col == 0 or col == len(lines) - 1:
        return True


new_obs = []


def check_for_loop(pos):
    row, col = pos[0][0], pos[0][1]
    direction = pos[1]
    # [print(line) for line in lines]
    # print("\n")
    # if direction == 'up' and lines[row][col + 1] == '-':
    #     print('up')
    #     new = [row - 1, col]
    #     if new not in new_obs:
    #         new_obs.append(new)
    #     return True
    # elif direction == 'down' and lines[row][col - 1] == '-':
    #     print('down')
    #     new = [row + 1, col]
    #     if new not in new_obs:
    #         new_obs.append(new)
    #     return True
    # elif direction == 'right' and lines[row - 1][col] == '|':
    #     print('right')
    #     new = [row, col + 1]
    #     if new not in new_obs:
    #         new_obs.append(new)
    #     return True
    # elif direction == 'left' and lines[row - 1][col] == '|':
    #     print('left')
    #     new = [row, col - 1]
    #     if new not in new_obs:
    #         new_obs.append(new)
    #     return True

    if direction == 'up':
        for c in range(len(lines[row]) - 1):
            if lines[row][c] in ('|') and lines[row][c + 1] == '#' and lines[row - 1][c] == '|':
                new = [row + 1, col]
                if new not in new_obs:
                    new_obs.append(new)
                    return True
                break
    elif direction == 'down':
        for c in range(len(lines[row]) - 1):
            if lines[row][c] in ('|') and lines[row][c - 1] == '#' and lines[row + 1][c] == '|':
                new = [row - 1, col]
                if new not in new_obs:
                    new_obs.append(new)
                    return True
                break
    elif direction == 'right':
        for r in range(len(lines) - 1):
            if lines[r][col] in ('-') and lines[r + 1][col] == '#' and lines[r][col + 1] == '-':
                new = [row, col - 1]
                if new not in new_obs:
                    new_obs.append(new)
                    return True
                break
    elif direction == 'left':
        for r in range(len(lines) - 1):
            if lines[r][col] in ('-') and lines[r - 1][col] == '#' and lines[r][col - 1] == '-':
                new = [row, col + 1]
                if new not in new_obs:
                    new_obs.append(new)
                    return True
                break

    return False


total = 0

while True:
    pos = get_guard_pos()
    row, col = pos[0][0], pos[0][1]
    if pos[1] == 'up':
        lines[row - 1][col] = '^'
        lines[row][col] = '|'
        total += 1
    elif pos[1] == 'down':
        lines[row + 1][col] = 'v'
        lines[row][col] = '|'
        total += 1
    elif pos[1] == 'right':
        lines[row][col + 1] = '>'
        lines[row][col] = '-'
        total += 1
    elif pos[1] == 'left':
        lines[row][col - 1] = '<'
        lines[row][col] = '-'
        total += 1

    pos = get_guard_pos()
    row, col = pos[0][0], pos[0][1]
    # [print(line) for line in lines]
    check_for_loop(pos)
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

#     print(pos)


#     print('\n')

    if row == 0 or row == len(lines) - 1 or col == 0 or col == len(lines) - 1:
        break


pos = get_guard_pos()


total = 1
for line in lines:
    total += line.count('X')

print(new_obs)

print(len(new_obs))
