# there's some performance gain possible by not editing the grid

lines = [line.rstrip() for line in open('input.txt').readlines()]

lines = [list(line) for line in lines]

guards = "^>v<"

lines_backup = [line[:] for line in lines]


def get_pos(lines):
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] in guards:
                return [row, col]
    return [0, 0]


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_dir(l, row, col):
    guard = l[row][col]
    return dirs[guards.index(guard)]


l_pos = []

guard_pos = get_pos(lines)
while True:
    row, col = guard_pos[0], guard_pos[1]
    if row in [0, len(lines) - 1] or col in [0, len(lines[row]) - 1]:
        break
    direction = get_dir(lines, row, col)
    d_row, d_col = direction[0], direction[1]
    if lines[row + d_row][col + d_col] == "#":
        if guards.index(lines[row][col]) + 1 == len(guards):
            lines[row][col] = guards[0]
        else:
            lines[row][col] = guards[guards.index(lines[row][col]) + 1]
        continue
    else:
        lines[row + d_row][col + d_col] = lines[row][col]
        guard_pos = [row + d_row, col + d_col]

    lines[row][col] = "X"
    if [row, col] not in l_pos:
        l_pos.append([row,col])

l_pos.append(guard_pos)

total = 0

for pos in l_pos[1:]:
    row_pos, col_pos = pos[0], pos[1]
    lines_copy = [line[:] for line in lines_backup]
    lines_copy[row_pos][col_pos] = '#'
    switch_pos = []
    guard_pos = get_pos(lines_copy)
    while True:
        row, col = guard_pos[0], guard_pos[1]
        if switch_pos.count([row, col]) > 2:  # in loop
            total += 1
            break
        if row in [0, len(lines_copy) - 1] or col in [0, len(lines_copy[row]) - 1]:
            break
        direction = get_dir(lines_copy, row, col)
        d_row, d_col = direction[0], direction[1]
        if lines_copy[row + d_row][col + d_col] == "#":
            if guards.index(lines_copy[row][col]) + 1 == len(guards):
                lines_copy[row][col] = guards[0]
            else:
                lines_copy[row][col] = guards[guards.index(lines_copy[row][col]) + 1]
                switch_pos.append([row, col])
            continue
        else:
            lines_copy[row + d_row][col + d_col] = lines_copy[row][col]
            lines_copy[row][col] = "X"
            guard_pos = [row + d_row, col + d_col]


print(total)
