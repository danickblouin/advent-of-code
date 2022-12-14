# STARTED BUT NOT FINISHED
class Monkey:
    items = []
    operation = ""
    test = ""
    if_true = ""
    if_false = ""
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false


def part_one(lines):
    list_monkeys_lines = get_list_monkeys_values(lines)
    for monkey_values in list_monkeys_lines:
        print("\n")
        print(monkey_values)





def get_list_monkeys_values(lines):
    list_monkeys, list_values = [], []
    for idx,line in enumerate(lines):
        if idx % 6 == 0:
            if list_values:
                list_monkeys.append(list_values)
            list_values = []
        else:
            list_values.append(line)
    print(list_monkeys)
    return list_monkeys




if __name__ == "__main__":
    with open("test.txt") as file:
        lines = [line.strip() for line in file.readlines() if line.strip() != '']
        part_one(lines)
