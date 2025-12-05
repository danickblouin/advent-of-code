with open('test.txt', 'r') as file:
	lines = file.readlines()

	count = 0
	result = 0
	for line in lines:
		line = line.strip()
		ranges = line.split(',')
		for r in ranges:
			r = r.split('-')
			if r == ['']:
				continue
			m = int(r[0])
			ma = int(r[1])

			for i in range(m, ma+1):
				string = str(i)
				n = len(string)

				if string in (string + string)[1:-1]:
					result += i
					continue

				if n % 2 != 0:
					continue

				mid = n // 2
				start = string[:mid]
				end = string[mid:]

				if start.startswith("0") or end.startswith("0"):
					continue

				if int(start) == int(end):
					count += 1
					result += i

	print(result)
