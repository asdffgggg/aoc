input = open("2015/5.txt","r").read()

def nice(line):
    if any(s in line for s in ["ab", "cd", "pq", "xy"]):
        return False
    if len(list(x for x in line if x in "aeiou")) < 3:
        return False
    return any(chr(s) * 2 in line for s in range(ord("a"), ord("z") +1))

def part1(input):
    nicecounter = 0
    for line in input.splitlines():
        if nice(line):
            nicecounter += 1
    return nicecounter
        



def nice2(line):
    for i in range(len(line) - 1):
        if line[i:i+2] in line[i+2:]:
            break
    else:
        return False
    for i in range(len(line)- 2):
        if line[i] == line[i+2]:
            return True
    return False


def part2(input):
    nicecounter = 0
    for line in input.splitlines():
        if nice2(line):
            nicecounter += 1
    return nicecounter

print(part2(input))