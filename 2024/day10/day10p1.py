lines = [line.rstrip() for line in open('test2.txt').readlines()]

lines = [list(line) for line in lines]


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

start_pos = []

[print(line) for line in lines]

for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] == '0':
            start_pos.append([row, col])

last_number = '0'
for idx, pos in enumerate(start_pos):
    row, col = pos
    number = 0
    print(row, col)

    for direction in dirs:
        d_row, d_col = direction

        new_row, new_col = row + d_row, col + d_col
        print(new_row, new_col)

        if d_row >= 0 and d_col >= 0 and d_row < len(lines) and d_col < len(lines[row]):
            if lines[new_row][new_col] == number + 1:
                print('yes')












    # while lines[row][col] != '.' and lines[row][col] != '9':
    #     for direction in dirs:
    #         d_row, d_col = direction
    #         new_row, new_col = row + d_row, col + d_col
    #         if lines[new_row][new_col] == '.':
    #             continue
    #         # print(lines[new_row][new_col])
    #         # if lines[row + d_row][col + d_col] == str(int(last_number) + 1):
    #         last_number = lines[new_row][new_col]
    #         # new_row, new_col = new_row + d_row, new_col + d_col
    #         print(row, col)
    #         row, col = new_row + d_row, new_col + d_col

    #         # row, col = new_row, new_col
    #     if int(lines[row][col]) != number + 1:
    #         break
    #     number += 1
    # # break
