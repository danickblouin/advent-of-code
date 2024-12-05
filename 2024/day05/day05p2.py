lines = open('input.txt').read().rstrip().split('\n\n')

rules = [i.split('|') for i in lines[0].split('\n')]
lists = [i.split(',') for i in lines[1].split('\n')]

total = 0

corrected = []

def check_valid(l, swapped):
    new_list = []
    for r in rules:
        first = r[0]
        second = r[1]

        # check if valid
        if first in l and second in l:
            idx_first = l.index(first)
            idx_second = l.index(second)

            if idx_second < idx_first:
                new_list = l.copy()
                # swap
                new_list[idx_first] = second
                new_list[idx_second] = first

                return check_valid(new_list, True)
    if swapped:
        return l


for ll in lists:
    result = check_valid(ll, False)
    if result:
        corrected.append(result)

for ll in corrected:
    idx = int((len(ll) - 1) / 2)
    total += int(ll[idx])

print(total)
