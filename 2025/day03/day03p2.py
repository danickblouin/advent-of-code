lines = [line.rstrip() for line in open('input.txt').readlines()]

total = 0

to_find = 12

for bank in lines:
	batt = list(bank)

	res = []
	start = 0

	rest = to_find

	while rest > 0:
		end = len(batt) - rest

		m = ""
		max_index = -1

		for i in range(start, end + 1):
			if batt[i] > m:
				m = batt[i]
				max_index = i

		res.append(m)

		start = max_index + 1
		rest -= 1

		
	total += int("".join(res))

print(total)
