ex = "eedadn\ndrvtee\neandsr\nraavrd\natevrs\ntsrnev\nsdttsa\nrasrtv\nnssdts\nntnada\nsvetve\ntesnvt\nvntsnd\nvrdear\ndvrsen\nenarar"
input = open("6.txt","r").read()
def part1(input):
    n = len(input.split("\n", 1)[0])
    counts = [{} for _ in range(n)]
    for line in input.splitlines():
        
        for i, c in enumerate(line):
            if c not in counts[i]:
                counts[i][c] = 0
            counts[i][c] += 1
    
    for w in counts:
        maxcount = 0
        maxcount = min(w, key=w.get)
        print(maxcount)
    print( counts)
    

part1(input)