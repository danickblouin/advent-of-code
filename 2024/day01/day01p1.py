with open('input.txt', 'r') as file:
    # lines = [line.rstrip() for line in file]
    # print(lines)
    lines = []
    col1 = []
    col2 = []
    for line in file:
        line = line.rstrip().split('   ')
        col1.append(int(line[0]))
        col2.append(int(line[1]))

col1.sort()
col2.sort()

total = 0
for i, n in enumerate(col1):
    distance = abs(col1[i] - col2[i])
    total += distance

print(total)
