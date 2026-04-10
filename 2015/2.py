ex = "2x3x4\n1x1x10"

input = open("2015/2.txt","r").read()

def part1(input):
    ourbignum = 0
    for line in input.splitlines():

        dims =[int(i) for i in line.split("x")]
        sideareas = [dims[0] * dims[1],  dims[2] * dims[1], dims[2] * dims[0] ]
        ourbignum += min(sideareas) + 2 * sum(sideareas)
    return ourbignum



def part2(input):
    ourbignum = 0
    for line in input.splitlines():

        dims =[int(i) for i in line.split("x")]
        sideareas = [dims[0] + dims[1],  dims[2] + dims[1], dims[2] + dims[0] ]
        ourbignum += 2*min(sideareas) + (dims[0]*dims[1]*dims[2])
    return ourbignum
print(part2(input))