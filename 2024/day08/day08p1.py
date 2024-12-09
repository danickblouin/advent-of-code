from collections import defaultdict

lines = [line.rstrip() for line in open('input.txt').readlines()]

lines = [list(line) for line in lines]


possi = defaultdict(list)

for row, line in enumerate(lines):
    for col, char in enumerate(lines[row]):
        if char != '.':
            possi[char].append((row, col))

total = 0

for values in possi.values():
    for coord in values:
        row, col = coord[0], coord[1]
        for next_cord in values:
            next_row, next_col = next_cord[0], next_cord[1]

            d_row, d_col = next_row - row, next_col - col

            if next_row + d_row >= 0:
                if next_col + d_col >= len(lines) or next_row + d_row >= len(lines):
                    break
                if lines[next_row + d_row][next_col + d_col] == '#':
                    total += 1
                if lines[next_row + d_row][next_col + d_col] == '.':
                    lines[next_row + d_row][next_col + d_col] = '#'
                    total += 1

print(total)
