# INSPIRED BY HYPER-NEUTRINO (watched his video)
# didn't have time to do it myself but wanted to understand how to do it so I went step by step by
# watching his video
def f(x, y):
    # if only x is a int
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return f([x], y)
    else:
        # if y is a int
        if type(y) == int:
            return f(x, [y])
    
    # if both of elements are list we need to call the function recursively
    # zip goes iterates through each elements of both lists [a,b,c][d,e,f] => [a,d]
    # stops if one of the list is shorter than the other
    for a, b in zip(x, y):
        v = f(a, b)
        # if they're not equivalent
        if v:
            return v
    
    return len(x) - len(y)

def part_one(data):

    total = 0

    # foreach pairs that we have
    # idx because we need to get the sum of the indexes
    for idx, (a, b) in enumerate(data):
        if f(eval(a), eval(b)) < 0:
            # +1 because we need to start with the index 1 in the problem
            total += idx + 1

    print("PART ONE:", total)

# we need to keep track of how many items comes before each one
def part_two(data):
    index2 = 1
    index6 = 2

    for item in data:
        if f(item, [[2]]) < 0:
            index2 += 1
            # if item comes before [[2]], [[6]] must come after too 
            index6 += 1
        # if items comes before [[6]] but not before [[2]]
        elif f(item, [[6]]) < 0:
            index6 += 1
    print("PART TWO:", index2 * index6)


if __name__ == "__main__":
    # \n\n so we get the pairs
    data = list(map(str.splitlines, open("input.txt").read().strip().split("\n\n")))
    part_one(data)
    # we remove the split for \n\n
    data = list(map(eval, open("input.txt").read().split()))
    part_two(data)
