lines = open('test.txt').read().rstrip().split('\n\n')

rules = [i.split('|') for i in lines[0].split('\n')]
lists = [i.split(',') for i in lines[1].split('\n')]

total = 0

for l in lists:
    valid = True
    for r in rules:
        first = r[0]
        second = r[1]

        # check if valid
        if first in l and second in l:
            idx_first = l.index(first)
            idx_second = l.index(second)

            if idx_second < idx_first:
                valid = False
                print(first, second)
                break
    if valid:
        idx = int((len(l) - 1) / 2)
        total += int(l[idx])

print(total)
