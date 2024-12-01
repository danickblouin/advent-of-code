def part_one(lines):
    cycle_counter = 1
    list_number_of_cycles = []
    list_values = []
    x = 0
    for line in lines:
        cycle_to_add = 2 if "addx" in line else 1
        value_to_add = eval(line.split(" ")[1]) if cycle_to_add == 2 else 0
        x += value_to_add
        cycle_counter += cycle_to_add
        list_number_of_cycles.append(cycle_counter)
        list_values.append(x+1)

    cycle_to_check = [20,60,100,140,180,220]

    total = 0
    for cycle in cycle_to_check:
        if cycle in list_number_of_cycles:
            i = list_values[list_number_of_cycles.index(cycle)]
            total += i * cycle
        elif cycle-1 in list_number_of_cycles:
            i = list_values[list_number_of_cycles.index(cycle-1)]
            total += i * (cycle)
        elif cycle-2 in list_number_of_cycles:
            i = list_values[list_number_of_cycles.index(cycle-2)]
            total += i * (cycle)

    print("Part One: {}".format(total))



if __name__ == "__main__":
    with open("test.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        part_one(lines)
