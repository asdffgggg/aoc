ex = "^v^v^v^v^v"
input = open("2015/3.txt","r").read()

def part1(input):
    change = [0,0]
    placesyoucantpronounce = {tuple(change)}
    for i in input:
        match i:
            case "^":
                change[1] += 1
            case "v":
                change[1] -= 1
            case ">":
                change[0] += 1
            case "<":
                change[0] -= 1
        placesyoucantpronounce.add(tuple(change))
    return len(placesyoucantpronounce)


def part2(input):
    change = [0,0]
    roboschange = [0,0]
    robosanta = False
    placesyoucantpronounce = {tuple(change)}
    for i in input:
        c = roboschange if robosanta else change
        robosanta = not robosanta
        match i:
            case "^":
                c[1] += 1
            case "v":
                c[1] -= 1
            case ">":
                c[0] += 1
            case "<":
                c[0] -= 1
        placesyoucantpronounce.add(tuple(c))
    return len(placesyoucantpronounce)
print(part2(input))



