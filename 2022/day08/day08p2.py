# im getting too much
grid = [list(x) for x in open("input.txt").read().strip().splitlines()]


# visible if all tree between it and the edge are shorter
# just same row or col

# get total from edge
total = len(grid[0]) + len(grid[len(grid)-1]) + 2 * (len(grid) -2)


maxi = 0
for row in range(len(grid)):
    for column in range(len(grid)):
        tree = grid[row][column]

        # up and down
        total_up = 0
        total_down = 0
        total_right = 0
        total_left = 0

        for x in range(row):
            total_up += 1
            if grid[x][column] > tree:
                break
        for x in range(row + 1, len(grid)):
            total_down += 1
            if grid[column][x] > tree:
                break

        for x in range(column):
            total_right += 1
            if grid[row][x] > tree:
                break

        for x in range(column + 1, len(grid)):
            total_left += 1
            if grid[row][x] > tree:
                break

        tt = total_up * total_down * total_right * total_left
        if tt > maxi:
            maxi = tt

print(maxi)
