import math
from datetime import datetime

start_time = datetime.now()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]

if not lines:
    exit()

operations = lines[-1].split()
grid = [line for line in lines[:-1] if '+' not in line]

columns = ["".join(col).strip() for col in zip(*grid)]

columns.append("")

total = 0
current_group = []
op_idx = 0

for val in columns:
    if not val:
        if current_group:
            nums = [int(n) for n in current_group]
            op = operations[op_idx]
            
            if op == "+":
                total += sum(nums)
            else:
                total += math.prod(nums)
            
            op_idx += 1
            current_group = []
    else:
        current_group.append(val)


print(total)
print(f"{(datetime.now() - start_time).microseconds / 1000} ms")
