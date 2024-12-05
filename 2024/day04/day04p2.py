lines = open('input.txt').read().rstrip().splitlines()

total = 0

diag_right = []
diag_left = []

for row in range(1, len(lines) - 1):
    for col in range(1, len(lines) - 1):
        middle = lines[row][col]
        top_left = lines[row - 1][col - 1]
        top_right = lines[row - 1][col + 1]
        bottom_left = lines[row + 1][col - 1]
        bottom_right = lines[row + 1][col + 1]

        diag_right.append("".join([top_left, middle, bottom_right]))
        diag_left.append("".join([top_right, middle, bottom_left]))

for i in range(len(diag_right)):
    if (diag_right[i] == "MAS" or diag_right[i] == "SAM") and (diag_left[i] == "MAS" or diag_left[i] == "SAM"):
        total += 1

print(total)
