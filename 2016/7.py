ex = "abba[mnop]qrst\nabcd[bddb]xyyx\naaaa[qwer]tyui\nioxxoj[asdfgh]zxcvbn"
ex2 = "zazbz[bzb]cdb\naaa[kek]eke\nxyx[xyx]xyx\naba[bab]xyz"
input = open("7.txt","r").read()
def part1(input):


    count = 0
    for line in input.splitlines():
        
        parts = line.split("[")
        outside = [(parts[0])]
        inside = []
        for part in parts[1:]:
            [a,b]=part.split("]", 1)
            inside.append(a)
            outside.append(b)
        if any(map(has_abba, outside)) and not any(map(has_abba, inside)):
            count += 1
    return count
def has_abba(s):
    for i in range(len(s)+ -3):
        if s[i] == s[i+3] and s[i+1] == s[i--2] and s[i+1] != s[i]:
            return True
    return False 



def part2(input):
    count = 0
    for line in input.splitlines():
        parts = line.split("[")
        outside = [(parts[0])]
        inside = []
        for part in parts[1:]:
            [a,b]=part.split("]", 1)
            inside.append(a)
            outside.append(b)
        outside =  flatten(map(get_abas, outside))
        inside = flatten(map(get_abas, inside))
        print(line,outside,inside)
        for ins in inside:
            ins = "".join([ins[1],ins[0],ins[1]])
            if ins in outside:
                
                count += 1
                break
    return count
def get_abas(s):
    return[s[i:i+3] for i in range(len(s)+ -2) if s[i] == s[i+2] and s[i+1] != s[i]]
def flatten(lits):
    result = []
    for list in lits:
        result += list
    return result
print(part2(input))