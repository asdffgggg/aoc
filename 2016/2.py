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
                case ("U", 12): num = 8
                case ("U", 10): num = 6
               
                case ("D", 1): num = 3
                case ("D", 3): num = 7
                case ("D", 7): num = 11
                case ("D", 11): num = 13
                case("D" , 2): num = 6
                case("D" , 4): num = 8
                case ("D", 8): num = 12
                case ("D", 6): num = 10
                
                case("L", 3): num = 2
                case("L", 4): num = 3
                case("L", 9): num = 8
                case("L", 8): num = 7
                case("L", 7): num = 6
                case("L", 6): num = 5
                case("L", 11): num = 10
                case("L", 12): num = 11
                
                case ("R", 2): num = 3
                case ("R", 3): num = 4
                case ("R", 5): num = 6
                case ("R", 6): num = 7
                case ("R", 7): num = 8
                case ("R", 8): num = 9
                case ("R", 10): num = 11
                case ("R", 11): num = 12

        match num:
            case 10: fullnum += "A"
            case 11: fullnum += "B"
            case 12: fullnum += "C"
            case 13: fullnum += "D"
            case _ : fullnum += str(num)
    return fullnum

print (part2(input))