lines = [line.rstrip() for line in open('input.txt').readlines()]

mat = []
for line in lines:
    mat.append(list(line))

pos = []

directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

go = True
count = 0
while go:
    total = 0
    for row, r in enumerate(mat):
        for col, c in enumerate(r):
            if c == "@":
                values = []
                for direc in directions:
                    if values.count("@") > 4:
                        break
                    new_row = row + direc[0]
                    new_col = col + direc[1]
                    if new_row < 0 or new_col < 0 or new_row >= len(mat) or new_col >= len(mat[row]):
                        continue
                    values.append(mat[new_row][new_col])


                if values.count("@") < 4:
                    mat[row][col] = "."
                    pos.append([row, col])
                    total += 1
                    continue
    count += total
    if total == 0:
        go = False

print(count)
