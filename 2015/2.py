ex = "2x3x4\n1x1x10"

input = open("2015/2.txt","r").read()

def part1(input):
    for line in input.splitlines():
        dims =[int(i) for i in line.split("x")]
            
    