#   0 1 2 3 4 5 6 7 8 9
# 0 M M M S X X M A S M
# 1 M S A M X M S M S A
# 2 A M X S X M A A M M
# 3 M S A M A S M S M X
# 4 X M A S A M X A M M
# 5 X X A M M X X A M A
# 6 S M S M S A S X S S
# 7 S A X A M A S A A A
# 8 M A M M M X M M M M
# 9 M X M X A X M A S X

def get_count(string):
    return string.count("XMAS") + string.count("SAMX")


lines = open('input.txt').read().rstrip().splitlines()

total = 0

for line in lines:
    total += get_count(line)

diag_right = []
for i in range(len(lines)):
    col = i
    row = 0
    abc = []
    while row < len(lines) and col < len(lines[0]):
        abc.append(lines[row][col])
        row += 1
        col += 1
    diag_right.append("".join(abc))

for start_row in range(1, len(lines)):
    col, row = 0, start_row
    abc = []
    while row < len(lines) and col < len(lines[0]):
        abc.append(lines[row][col])
        row += 1
        col += 1
    diag_right.append("".join(abc))

diag_left = []
for i in range(len(lines)):
    col = len(lines) - 1 - i
    row = 0
    abc = []
    while row < len(lines) and col >= 0:
        abc.append(lines[row][col])
        row += 1
        col -= 1
    diag_left.append("".join(abc))

for start_row in range(1, len(lines)):
    col, row = len(lines[0]) - 1, start_row
    abc = []
    while row < len(lines) and col >= 0:
        abc.append(lines[row][col])
        row += 1
        col -= 1
    diag_left.append("".join(abc))

for t in diag_right:
    total += get_count(t)

for t in diag_left:
    total += get_count(t)

# vertical
vert = []
for col in range(len(lines)):
    list_vert = []
    for row in range(len(lines)):
        list_vert.append(lines[row][col])
    vert.append("".join(list_vert))

for t in vert:
    total += get_count(t)

print(f"Total: {total}")
