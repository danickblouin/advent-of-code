line = open('test.txt').readline().rstrip()

disk = []
index = 0
is_number = True

for char in line:
    count = int(char)
    if is_number:
        disk.extend([index] * count)
        index += 1
    else:
        disk.extend(['.'] * count)
    is_number = not is_number

for j in range(len(disk) - 1, 0, -1):
    if disk[j] != '.':
        disk[i] = disk[j]
        disk[j] = '.'
        break

for i in range(len(disk)):
    if disk[i] == '.':
        for j in range(len(disk) - 1, i, -1):
            if disk[j] != '.':
                disk[i] = disk[j]
                disk[j] = '.'
                break

total = 0
for pos, value in enumerate(disk):
    if value == '.':
        break
    total += pos * value
    
print(total)
