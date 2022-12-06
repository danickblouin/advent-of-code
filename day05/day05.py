array = []
# DIDN'T HAVE THE TIME TO FIND A WAY TO PARSE THE STACK DIRECTLY SO I DID THAT
def setarray():
    array = [
        ["R","N","F","V","L","J","S","M"],
        ["P","N","D","Z","F","J","W","H"],
        ["W","R","C","D","G"],
        ["N","B","S"],
        ["M","Z","W","P","C","B","F","N"],
        ["P","R","M","W"],
        ["R","T","N","G","L","S","W"],
        ["Q","T","H","F","N","B","V"],
        ["L","M","H","Z","N","F"]
        ]
    return array

def part_one(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines() if "move" in line]
        split = [line.split(" ") for line in lines]

        # NUMBER / FROM / TO
        moves = [[line[1],line[3], line[5]] for line in split]
        for move in moves:
            number,fromm,to = int(move[0]), int(move[1])-1, int(move[2])-1
            stack_to_remove_item = array[fromm]
            stack_to_add_item = array[to]
            for x in range(number):
                stack_to_add_item.append(stack_to_remove_item[-1])
                stack_to_remove_item.pop()

def part_two(path):
    with open(path) as file:
        lines = [line.strip() for line in file.readlines() if "move" in line]
        split = [line.split(" ") for line in lines]

        # NUMBER / FROM / TO
        moves = [[line[1],line[3], line[5]] for line in split]
        for move in moves:
            number,fromm,to = int(move[0]), int(move[1])-1, int(move[2])-1
            stack_to_remove_item = array[fromm]
            stack_to_add_item = array[to]
            stack_to_add_item.extend(stack_to_remove_item[-number:])
            for x in range(number):
                stack_to_remove_item.pop()

if __name__ == "__main__":
    input_path = "./day05/input.txt"
    array = setarray()
    part_one(input_path)
    print([line[-1] for line in array])
    array = setarray()
    part_two(input_path)
    print([line[-1] for line in array])