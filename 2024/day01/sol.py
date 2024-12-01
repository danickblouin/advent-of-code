# part 1

a = list(map(list, zip(*[list(map(int, line.split())) for line in open('input.txt', 'r').read().splitlines()])))

for k in a:
    k.sort()

print(sum(abs(x - y) for x, y in zip(*a)))

# part 2

l, r = list(map(list, zip(*[list(map(int, line.split())) for line in open('input.txt', 'r').read().splitlines()])))

print(sum(x * r.count(x) for x in l))
