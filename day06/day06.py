def unique(s):
    return len(set(s)) == len(s)

def part_one(lines):
    for x,char in enumerate(line):
        four = line[x:x+4]
        if unique(four):
            return line.index(four)+4

def part_two(lines):
    for x,char in enumerate(line):
        fourteen = line[x:x+14]
        if unique(fourteen):
            return line.index(fourteen)+14

if __name__ == "__main__":
    input_path = "./day06/input.txt"
    with open(input_path) as file:
        lines = [line.strip() for line in file.readlines()]
        for line in lines:
            print("PART ONE: {}".format(part_one(line)))
            print("PART TWO: {}".format(part_two(line)))
            break