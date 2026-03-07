example = "ULL\nRRDDD\nLURDL\nUUUUD"
input = open("2.txt","r").read()
def part1(input):
    fullnum = ""
    num = 5
    for line in input.splitlines():
        for i in line:
            match i:
                case "U":  
                    if num > 3:  
                        num -= 3
                case "D":
                    if num < 7:
                        num +=3       
                case "L":
                    if num%3 != 1:
                        num -=1       
                case "R":  
                    if num%3 != 0:
                        num +=1     
        fullnum += str(num)
    return fullnum
def part2(input):
    fullnum = ""
    num = 5
    for line in input.splitlines():
        for i in line:
            match (i, num):
                case ("U", 3): num = 1
                case ("U", 7): num = 3
                case ("U", 11): num = 7
                case ("U", 13): num = 11
                case ("U", 6): num = 2
                case ("U", 8): num = 4
                case ("D", 1): num = 3
                case ("D", 3): num = 7
                case ("D", 7): num = 11
                case ("D", 11): num = 13
                case("D" , 2): num = 6
                case("D" , 4): num = 8
                case("L", 3): num = 2
                case("L", 4): num = 3
                case("L", 9): num = 8
                case("L", 8): num = 7
                case("L", 7): num = 6
                case("L", 6): num = 5
                
                case("L", 11): num = 10
                case("L", 12): num = 11

            
        fullnum += str(num)
    return fullnum

print (part1(input))