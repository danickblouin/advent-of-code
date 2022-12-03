# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

# 1 = Rock
# 2 = Paper
# 3 = Scissors

# 0 = lost
# 3 = draw
# 6 = win

def part_one(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]

    point = 0
    for line in lines:
        two = line.split(" ")
        other = two[0]
        me = two[1]
        # friday night no thinking available
        # ROCK
        if (me == "X"):
            point += 1 
            if other == "A":
                point += 3
            elif other == "C":
                point += 6
        # PAPER
        elif me == "Y":
            point += 2
            if other == "B":
                point += 3
            elif other == "A":
                point += 6
        # SCISSORS
        elif me == "Z":
            point += 3
            if other == "B":
                point += 6
            elif other == "C":
               point += 3 
        if me == "B" and other == "X":
            print ("TEST" + point)
    print("PART ONE:" + str(point))

# # X = loose
# # Y = draw
# # Z = win
# def part_two(path):
#     with open(path) as file:
#         lines = [line.strip() for line in file.readlines()]
#     for line in lines:
#         two = line.split(" ")
#         other = two[0]
#         me = two[1]
#         point = 0
#         if other == "A":
#             if me == "X"
#         elif other == "B":
#         elif other == "C":
#     print("PART TWO:" + str(point))

if __name__ == "__main__":
    input_path = "./day02/input.txt"
    part_one(input_path)
    part_two(input_path)