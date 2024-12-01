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

total = 0
for i, n in enumerate(col1):
    count = 0
    for number in col2:
        if n == number:
            count += 1

    total += n * count

print(total)
