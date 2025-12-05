lines = [line.rstrip() for line in open('input.txt').readlines()]


total = 0

for bank in lines:
	batt = list(bank)
	
	m = 0
	for i in range(len(batt)-1):
		n = batt[i]
		for x in range(i+1, len(batt)):
			y = batt[x]
			number = int(str(n) + str(y))
			if number > m:
				m = number
	total += m

print(total)
