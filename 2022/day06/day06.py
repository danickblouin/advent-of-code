def unique(s):
    return len(set(s)) == len(s)

def main(lines,size):
    for x,char in enumerate(line):
        text = line[x:x+size]
        if unique(text):
            return line.index(text)+size

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        for line in lines:
            print("PART ONE: {}".format(main(line,4)))
            print("PART TWO: {}".format(main(line,14)))
            break