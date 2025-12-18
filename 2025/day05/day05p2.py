lines = [line.rstrip() for line in open('input.txt').readlines()]

ranges = []
for line in lines:
    if line == "":
        break
    start = int(line.split('-')[0])
    end = int(line.split('-')[1])
    ranges.append([start, end])

ranges.sort()

good_ranges = []
seen = []

count = 0

for idx, r in enumerate(ranges):
    s = r[0]
    e = r[1]

    in_range = True

    new_e = e
    
    idx2 = idx + 1
    if r not in seen:
        while in_range:
            if idx2 == len(ranges):
                break
            r2 = ranges[idx2]
            if r2 not in seen:
                s2 = r2[0]
                e2 = r2[1]

                if new_e < s2:
                    in_range = False
                elif e2 < new_e:
                    seen.append(r2)
                    in_range = True
                else:
                    new_e = e2
                    seen.append(r2)
                    in_range = True

            idx2 += 1

        good_ranges.append([s, new_e])
        count += new_e - s + 1

print(count)
