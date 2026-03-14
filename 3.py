import itertools
ex = " 5 10 25\n10 15 21\n 4 9 8"
input = open("3.txt","r").read()
def part1(input):
    possibletri = 0
    for line in input.splitlines():
        sides = [int(word) for word in line.split()]
        if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[2] + sides[1] > sides[0]:
            possibletri += 1
    return possibletri
        
print(part1(input))


def part2(input):
    possibletri = 0
    for chunk in itertools.batched(input.splitlines(), 3):
        chunk = [line.split() for line in chunk]
        for i in range(3):
            sides = [int(line[i]) for line in chunk]
            if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[2] + sides[1] > sides[0]:
                possibletri += 1
    return possibletri
print(part2(input))
