ex = "())"
input = open("2015/1.txt","r").read()
def part1(input):
    counter = 0
    for i in input:
        if i == "(":
            counter +=1
        elif i == ")":
            counter -= 1
    return counter


def part2(input):
    counter = 0
    for i,h in enumerate(input):
        if h == "(":
            counter +=1
        elif h == ")":
            counter -= 1
        if counter == -1:
            return i + 1
        
print(part2(input))