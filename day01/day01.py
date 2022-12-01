def read_file(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]

    array = []
    tempsum = 0
    for line in lines:
        if not line.strip():
            tempsum = 0
        else:
            tempsum += int(line.strip())
        array.append(tempsum)
    array.sort(reverse=True)
    print("Part One:" + str(array[0]))
    totalTop3 = sum(array[:3])
    print("Part Two:" + str(totalTop3))

if __name__ == "__main__":
    input_path = "./day01/input.txt"
    read_file(input_path)