ex = "eedadn\ndrvtee\neandsr\nraavrd\natevrs\ntsrnev\nsdttsa\nrasrtv\nnssdts\nntnada\nsvetve\ntesnvt\nvntsnd\nvrdear\ndvrsen\nenarar"

def part1(input):
    n = len(input.split("\n", 1)[0])
    counts = [{} for _ in range(n)]
    for line in input.splitlines():
        for i, c in enumerate(line):
            if c not in counts[i]:
                counts[i][c] = 0
            counts[i][c] += 1
    print( counts)

part1(ex)