lines = [line.rstrip() for line in open('input.txt').readlines()]

lines = [list(line) for line in lines]

guards = "^>v<"


def get_pos(lines):
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] in guards:
                return [row, col]


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_dir(row, col):
    guard = lines[row][col]
    return dirs[guards.index(guard)]


l_pos = []

while True:
    pos = get_pos(lines)
    row, col = pos[0], pos[1]
    if row in [0, len(lines) - 1] or col in [0, len(lines[row]) - 1]:
        break
    direction = get_dir(row, col)
    d_row, d_col = direction[0], direction[1]
    if lines[row + d_row][col + d_col] == "#":
        if guards.index(lines[row][col]) + 1 == len(guards):
            lines[row][col] = guards[0]
        else:
            lines[row][col] = guards[guards.index(lines[row][col]) + 1]
        continue
    else:
        lines[row + d_row][col + d_col] = lines[row][col]

    lines[row][col] = "X"
    if [row, col] not in l_pos:
        l_pos.append([row,col])

print(len(l_pos) + 1)
