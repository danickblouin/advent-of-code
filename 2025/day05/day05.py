lines = [line.rstrip() for line in open('input.txt').readlines()]

switch = False

ranges = []
ing = []
for line in lines:
    if line == "":
        switch = True
        continue
    if not switch:
        ranges.append(line)
    else:
        ing.append(line)

print(ranges)
print(ing)

seen = []
for i in ing:
    i = int(i)
    for r in ranges:
        start = int(r.split('-')[0])
        end = int(r.split('-')[1])

        print(start, end, i)
        if i >= start and i <= end and i not in seen:
            print("VALID", i, r)
            seen.append(i)

print(seen)
print(len(seen))
