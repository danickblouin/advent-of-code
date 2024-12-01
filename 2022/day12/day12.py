# INSPIRED BY HYPER-NEUTRINO
# using Breadth-first search (https://en.wikipedia.org/wiki/Breadth-first_search)
from collections import deque

def part_one(grid):
    start_row, start_column, end_column, end_row = 0,0,0,0
    # FIND START AND END
    for i,row in enumerate(grid):
        for c,char in enumerate(row):
            if char == "S":
                start_row = i
                start_column = c
                # change the value so we don't have to deal with the S
                grid[i][c] = "a"
            if char == "E":
                end_row = i
                end_column = c
                # change the value so we don't have to deal with the E
                grid[i][c] = "z"

    q = deque()

    # size of travel and current pos
    q.append((0, start_row, start_column))

    # keep list of visited nodes
    # use set instead of simple array cause it's faster
    visited = {(start_row, start_column)}

    while q:
        distance, row, column = q.popleft()
        # we test each side of the current position
        for next_row, next_column in [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]:
            # check if next_row and next_column are in the bounds of the grid
            if next_row < 0 or next_row >= len(grid) or next_column < 0 or next_column >= len(grid[0]):
                continue
            # if we already checked it
            if (next_row, next_column) in visited:
                continue
            # if the difference in height is begger than 1
            # ord returns the letter's value in int
            if ord(grid[next_row][next_column]) - ord(grid[row][column]) > 1:
                continue
            # if were at the destination
            if next_row == end_row and next_column == end_column:
                print(distance+1)
                break
            visited.add((next_row, next_column))
            q.append((distance+1, next_row, next_column))

# do the same thing as part_one but start at the end instead and find the fist position = 'a' 
def part_two(grid):
    start_row, start_column = 0, 0
    for i, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "E":
                start_row = i
                start_column = c
                grid[i][c] = "z"

    q = deque()

    q.append((0, start_row, start_column))

    visited = {(start_row, start_column)}

    while q:
        distance, row, column = q.popleft()
        for next_row, next_column in [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]:
            if next_row < 0 or next_row >= len(grid) or next_column < 0 or next_column >= len(grid[0]):
                continue
            if (next_row, next_column) in visited:
                continue
            if ord(grid[row][column]) - ord(grid[next_row][next_column]) > 1:
                continue
            if grid[next_row][next_column] == "a":
                print(distance+1)
                exit(0)
            visited.add((next_row, next_column))
            q.append((distance+1, next_row, next_column))
    
if __name__ == "__main__":
    grid = [list(x) for x in open("input.txt").read().strip().splitlines()]
    part_one(grid)
    grid = [list(x) for x in open("input.txt").read().strip().splitlines()]
    part_two(grid)
