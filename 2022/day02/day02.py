# NEED TO LEARN HOW TO USE PYTHON PROPERLY
from enum import Enum

class Item(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

class Points(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class ToDo(Enum):
    LOOSE = "X"
    DRAW = "Y"
    WIN = "Z"

class Points(Enum):
    LOOSE = 0
    DRAW = 3
    WIN = 6

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

def part_two(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]

    point = 0
    for line in lines:
        two = line.split(" ")
        other = two[0]
        toplay = two[1]
        if toplay == ToDo.LOOSE.value:
            if other == Item.ROCK.value:
                point += 3
            elif other == Item.PAPER.value:
                point += 1
            else:
                point += 2
        elif toplay == ToDo.DRAW.value:
            point += Points.DRAW.value
            if other == Item.ROCK.value:
                point += 1
            elif other == Item.PAPER.value:
                point += 2
            else:
                point += 3
        elif toplay == ToDo.WIN.value:
            point += Points.WIN.value
            if other == Item.ROCK.value:
                point += 2
            elif other == Item.PAPER.value:
                point += 3
            else:
                point += 1
    print("PART TWO:" + str(point))

if __name__ == "__main__":
    input_path = "./day02/input.txt"
    part_one(input_path)
    part_two(input_path)