# with open('test.txt', 'r') as file:
with open('input.txt', 'r') as file:
    lines = file.readlines()
    start = 50
    count = 0
    for line in lines:
        line = line.strip()
        direction = line[0]
        number = int(line[1:])
        print(start, direction, number)

        if direction == "L":
            start -= number
            while start < 0:
                left = 100 + start
                start = 0 + left
        else:
            start += number
            while start > 99:
                left = start - 100
                start = 0 + left
        if start == 0:
            count += 1


    print(count)
