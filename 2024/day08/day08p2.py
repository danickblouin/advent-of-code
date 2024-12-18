from collections import defaultdict

lines = [line.rstrip() for line in open('input.txt').readlines()]

lines = [list(line) for line in lines]


possi = defaultdict(list)

for row, line in enumerate(lines):
    for col, char in enumerate(lines[row]):
        if char != '.':
            possi[char].append((row, col))

anti = set()

for values in possi.values():
    for coord in values:
        row, col = coord[0], coord[1]
        for next_coord in values:
            if coord == next_coord:
                continue
            next_row, next_col = next_coord[0], next_coord[1]
            d_row, d_col = next_row - row, next_col - col
            
            curr_row, curr_col = row, col
            while 0 <= curr_row < len(lines) and 0 <= curr_col < len(lines):
                anti.add((curr_row, curr_col))
                curr_row += d_row
                curr_col += d_col

print(len(anti))
