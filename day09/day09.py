if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        for line in lines:
            print(line)
