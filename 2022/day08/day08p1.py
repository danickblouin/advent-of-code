grid = [list(x) for x in open("input.txt").read().strip().splitlines()]


# visible if all tree between it and the edge are shorter
# just same row or col

# get total from edge
total = len(grid[0]) + len(grid[len(grid)-1]) + 2 * (len(grid) -2)

for row in range(1, len(grid)-1):
    for column in range(1, len(grid)-1):
        tree = grid[row][column]

        # up and down
        a = all(grid[x][column] < tree for x in range(row)) or all(grid[x][column] < tree for x in range(row + 1, len(grid)))
        # right and left
        b = all(grid[row][x] < tree for x in range(column)) or all(grid[row][x] < tree for x in range(column + 1, len(grid)))
        if a or b:
            total += 1

print(total)
