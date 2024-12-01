def answer(path):
    with open(path) as file:
        # lines = list(dict.fromkeys([line.strip() for line in file.readlines()]))
        lines = [line.strip() for line in file.readlines()]
        count = 0
        count_total = 0
        
        for line in lines:
            split = line.split(',')
            one, two, one_two, two_two = int(split[0].split('-')[0]), int(split[0].split('-')[1]), int(split[1].split('-')[0]), int(split[1].split('-')[1])

            if (one <= one_two and two >= two_two) or (one >= one_two and two <= two_two):
                count+=1
            if (two >= one_two and one <= two_two):
                count_total += 1                

        print(count)
        print(count_total)

if __name__ == "__main__":
    input_path = "./day04/input.txt"
    answer(input_path)