lines = [line.rstrip() for line in open('input.txt').readlines()]

mat = []
for line in lines:
    mat.append(list(line))

pos = []

directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

total = 0
for row in range(len(mat)):
    for col in range(len(mat[row])):
        if mat[row][col] == "@":
            values = []
            for direc in directions:
                new_row = row + direc[0]
                new_col = col + direc[1]
                if new_row == -1 or new_col == -1:
                    continue
                try:
                    values.append(mat[new_row][new_col])
                except:
                   continue

            if values.count("@") < 4:
                pos.append([row, col])
                total += 1

print(total)

