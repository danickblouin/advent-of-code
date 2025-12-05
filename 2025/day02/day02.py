with open('input.txt', 'r') as file:
    lines = file.readlines()

    count = 0
    result = 0
    for line in lines:
        line = line.strip()
        ranges = line.split(',')
        for r in ranges:
            r = r.split('-')
            m = int(r[0])
            ma = int(r[1])

            for i in range(m, ma+1):
                string = str(i)
                n = len(str(i))
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
