import re


with open('input.txt', 'r') as f:
    lines = f.readlines()

    total = 0

    pattern = re.compile(r'mul\((\d+),(\d+)\)')

    for line in lines:
        for r in pattern.finditer(line):
            a, b = map(int, r.groups())
            total += a * b

    print(total)
