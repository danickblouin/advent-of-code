# watched hyper-neutrino video

def part_one(lines):
    # using a set is better cause with a grid we'll need to expend the grid
    # to the right size => easy to make bugs

    # we could use a dictionnary
    full = set()
    abyss = 0
    for line in lines:
        x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
        # get pairs of values
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            # sort them because they're not always in order
            x1,x2 = sorted([x1,x2])
            y1,y2 = sorted([y1,y2])
            # makes a rectangle but since x1=x2 or y1=y2 it creates a simple line
            for x in range(x1, x2+1):
                for y in range (y1, y2+1):
                    # we use complex numbers
                    # we set the x as the real value and the y as the imaginary value
                    # we could have done full.add((x,y))
                    full.add(x + y * 1j)
                    # if y+1 is bigger than the abyss we set the abyss to this point
                    abyss = max(abyss, y+1)

    total = 0
    run = True 
    while run:
        # 500 + 0j
        start = 500
        # keep droping the sand as long as we can
        while run:
            # if it goes in the abyss
            if start.imag >= abyss:
                print("PART ONE:",total)
                run = False
            # if below is not used
            if start + 1j not in full:
                start += 1j
                continue
            # if left below is not used
            if start + 1j - 1 not in full:
                start += 1j - 1
                continue
            # if right below is not used
            if start + 1j + 1 not in full:
                start += 1j + 1
                continue
            full.add(start)
            total += 1
            break


def part_two(lines):
    full = set()
    abyss = 0
    for line in lines:
        x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
        # get pairs of values
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            # sort them because they're not always in order
            x1,x2 = sorted([x1,x2])
            y1,y2 = sorted([y1,y2])
            # makes a rectangle but since x1=x2 or y1=y2 it creates a simple line
            for x in range(x1, x2+1):
                for y in range (y1, y2+1):
                    # we use complex numbers
                    # we set the x as the real value and the y as the imaginary value
                    full.add(x + y * 1j)
                    # if y+1 is bigger than the abyss we set the abyss to this point
                    abyss = max(abyss, y+1)

    total = 0
    
    while 500 not in full:
        # 500 + 0j
        start = 500
        # keep droping the sand as long as we can
        while True:
            # if it goes in the abyss
            if start.imag >= abyss:
                break
            # if below is not used
            if start + 1j not in full:
                start += 1j
                continue
            # if left below is not used
            if start + 1j - 1 not in full:
                start += 1j - 1
                continue
            # if right below is not used
            if start + 1j + 1 not in full:
                start += 1j + 1
                continue
            break
        # we put this here so we don't have to repeat it there and on the first if
        full.add(start)
        total += 1
    print("PART TWO:",total)

if __name__ == "__main__":
    lines = open("input.txt")
    part_one(lines)
    lines = open("input.txt")
    part_two(lines)
