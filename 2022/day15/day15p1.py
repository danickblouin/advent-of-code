# could use the regex pattern like that (way better)
# import re
# pattern = re.compile(r"-?\d+")
# sx, sy, bx, by = map(int, pattern.findall(line))

Y = 2000000

full = set()

for line in open("input.txt"):
    sensor_x = int(line.split(' ')[2].replace("x=","").replace(",",""))
    sensor_y = int(line.split(' ')[3].replace("y=","").replace(":",""))
    beacon_x = int(line.split(' ')[8].replace("x=","").replace(",",""))
    beacon_y = int(line.split(' ')[9].replace("y=","").replace(",",""))


    # using the formula to get the distance between two points
    # |x1-x2| + |y1-y2|
    distance = abs(sensor_x-beacon_x) + abs(sensor_y-beacon_y)

    offset = distance - abs(sensor_y - Y)

    # if the triangle doesn't affect the line that we're searching for
    if offset < 0:
        continue

    # we need to get the x coordinates of each place from the left of the scanner position and from the right too
    # x2 cause triangle
    for x in range(sensor_x-offset, sensor_x+offset):
        if x not in full:
            full.add(x)

print(len(full))
