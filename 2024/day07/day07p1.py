lines = [line.rstrip() for line in open('input.txt').readlines()]

lines = [[line.split(': ')[0], line.split(': ')[1].split(' ')] for line in lines]

result = 0


# checked hyperneutrino solution for hint
def check(total, numbers):
    if len(numbers) == 1:
        return numbers[0] == total
    if total % numbers[-1] == 0 and check(total // numbers[-1], numbers[:-1]):
        return True
    if total > numbers[-1] and check(total - numbers[-1], numbers[:-1]):
        return True

    return False


for line in lines:
    total = int(line[0])
    numbers = list(map(int, line[1]))
    if check(total, numbers):
        result += total


print(result)
