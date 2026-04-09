
ex = "aaaaa-bbb-z-y-x-123[abxyz]\na-b-c-d-e-f-g-h-987[abcde]\nnot-a-real-room-404[oarel]\ntotally-real-room-200[decoy]" 
input = open("4.txt","r").read()

def parse(input):
    data = []
    for line in input.splitlines():
        [left, right] = line.rsplit("-", 1)
        [sector, checksum]= right.split("[")
        sector = int(sector)
        checksum = checksum[:-1]
        data.append({
            "name": left, 
            "secid": sector,
            "checksum": checksum

        })
    return data

def validata(input):
    data = parse(input)
    newlist = []
    for d in data:
        counts = {}
        list = []
        for c in d["name"]:
            if c == "-":
                continue
            if c not in counts:
                counts[c] = 0
                list.append(c)
            counts[c] += 1
        list.sort(key = lambda c: (-counts[c], c))
        furstchecksum = "".join(list[:5])
        if furstchecksum == d["checksum"]:
            newlist.append(d)
    return newlist
    

def part1(input):
    return sum([d["secid"] for d in validata(input)])


def part2(input):
    for d in validata(input):
        decoded = ""
        for c in d["name"]:
        
            if c == "-":
                decoded += " "
            else:
                n = ord(c) - ord("a")
                n += d["secid"] 
                n %= 26
                decoded += chr(n+ord("a"))
        if "north" in decoded:
            return d["secid"]


print(part2(input))


