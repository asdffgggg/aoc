
input = open("1.txt","r").read()
def part1(input):
    x = 0
    y = 0
    dir = 0
    for i in input.split(", "):
        if i[0] == "R":
            dir += 1
        else:
            dir -= 1
        n = int(i[1:])
        if dir%4 == 0:
            y += n
        elif dir%4 == 1:
            x+= n
        elif dir%4 == 2:
            y -= n
        elif dir%4 == 3:
            x -= n
    return abs(x)+abs(y)

def part2(input):
    x = 0
    y = 0
    dir = 0
    visited = set()
    for i in input.split(", "):
        if i[0] == "R":
            dir += 1
        else:
            dir -= 1
        n = int(i[1:])
        for _ in range(n):
            if dir%4 == 0:
                y += 1
            elif dir%4 == 1:
                x+= 1
            elif dir%4 == 2:
                y -= 1
            elif dir%4 == 3:
                x -= 1
            if (x,y) in visited:
                return abs(x) + abs(y)
            visited.add((x,y))

print(part1("R20, L1, L1, L1"))
print(part2(input))
print(part2("R8, R4, R4, R8"))