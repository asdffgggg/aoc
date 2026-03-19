ex = "aaaaa-bbb-z-y-x-123[abxyz]\na-b-c-d-e-f-g-h-987[abcde]\nnot-a-real-room-404[oarel]\ntotally-real-room-200[decoy]" 
input = open("4.txt","r").read()
def part1(input):
    sum = 0
    for line in input.splitlines():
        [left, right] = line.rsplit("-", 1)
        counts = {}
        list = []
        for c in left:
            if c == "-":
                continue
            if c not in counts:
                counts[c] = 0
                list.append(c)
            counts[c] += 1
        list.sort(key = lambda c: (-counts[c], c))
        furstchecksum = "".join(list[:5])
        [sector, checksum]= right.split("[")
        sector = int(sector)
        checksum = checksum[:-1]
        if furstchecksum == checksum:
            sum += sector
    return sum
print(part1(input))