# got help from my friend chatgpt for this one
# it's based on my part 1 tho
lines = [list(line.rstrip()) for line in open('input.txt').readlines()]

guards = "^>v<"
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_start(lines):
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] in guards:
                return row, col, guards.index(lines[row][col])
    return None, None, None


start_row, start_col, start_dir = get_start(lines)

# Convert the guard's initial position to floor '.' and just store the position and direction separately
lines[start_row][start_col] = '.'


def simulate(l, obstacle_row=None, obstacle_col=None):
    # If we place an obstacle, do it now
    if obstacle_row is not None and obstacle_col is not None:
        original_char = l[obstacle_row][obstacle_col]
        l[obstacle_row][obstacle_col] = '#'
    else:
        original_char = None

    visited_states = set()
    # Guard's starting position and direction
    gr, gc, gdir = start_row, start_col, start_dir

    while True:
        state = (gr, gc, gdir)
        if state in visited_states:
            # Loop detected
            result = True
            break
        visited_states.add(state)

        # Check if guard is at the boundary
        if gr == 0 or gr == len(l) - 1 or gc == 0 or gc == len(l[0]) - 1:
            # Guard leaves the map
            result = False
            break

        d_row, d_col = dirs[gdir]
        front_cell = l[gr + d_row][gc + d_col]

        if front_cell == '#':
            # Turn right
            gdir = (gdir + 1) % 4
            # Don't move, just change direction
        else:
            # Move forward
            gr += d_row
            gc += d_col

    # Revert the obstacle if placed
    if obstacle_row is not None and obstacle_col is not None:
        l[obstacle_row][obstacle_col] = original_char

    return result


loop_count = 0

for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == '.' and not (r == start_row and c == start_col):
            if simulate(lines, r, c):
                loop_count += 1

print(loop_count)
