with open('input.txt', 'r') as file:
# with open('test.txt', 'r') as file:
    lines = file.readlines()
    current = 50
    count = 0

    for line in lines:
        line = line.strip()
        direction = line[0]
        number = int(line[1:])
        op = 0
        if direction == "L":
            op = -1
        else:
            op = 1

        for idx in range(number):
            current += op
            if current < 0:
                current = 99
            elif current > 99:
                current = 0

            if current == 0:
                count += 1

        print(line, current)


print(count)
