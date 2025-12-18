import numpy as np

lines = [line.rstrip() for line in open('input.txt').readlines()]

operations = lines[len(lines)-1].split()

mat = []
for line in lines:
    mat.append(line.split())

ll = np.array(mat)

matrix = ll.T.tolist()

total = 0
for l in matrix:
    op = l[-1]
    count = 0
    if op == "+":
        for i in range(len(l)-1):
            count += int(l[i])
    elif op == "*":
        for i in range(len(l)-1):
            if count == 0:
                count = int(l[i])
            else:
                count = count * int(l[i])

    total += count

print(total)
