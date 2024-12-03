import re


with open('input.txt', 'r') as f:
    lines = f.readlines()

    total = 0

    doing = True

    for line in lines:
        for r in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", line):
            if r == 'do()':
                doing = True
            elif r == "don't()":
                doing = False
            elif doing:
                a, b = map(int, r[4: len(r) - 1].split(','))
                total += a * b

    print(total)
