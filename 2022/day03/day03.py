# one empty for +1 when getting the index
letters = ['empty','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def part_one(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
    
    points = 0
    for line in lines:
        string1, string2 = line[:len(line)//2], line[len(line)//2:]
        for char in string1:
            if char in string2:
                points += letters.index(char)
                break
    print("PART ONE: {}".format(points))

def part_two(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
    
    counter = 1
    total_points = 0
    groups = []
    array = []
    for line in lines:
        array.append(line)
        if counter % 3 == 0:
            groups.append(array)
            array = []
        counter += 1
    
    for group in groups:
        points = 0
        string1, string2, string3 = group[0], group[1], group[2]

        for char in string1:
            if char in string2 and char in string3:
                points += letters.index(char)
                break
        total_points += points

    print("PART TWO: {}".format(total_points))

if __name__ == "__main__":
    input_path = "./day03/input.txt"
    part_one(input_path)
    part_two(input_path)